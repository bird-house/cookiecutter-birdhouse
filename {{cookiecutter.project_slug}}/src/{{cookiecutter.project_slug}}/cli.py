"""Demo WPS service for testing and debugging."""
###########################################################
# See the werkzeug documentation on how to use the debugger:
# http://werkzeug.pocoo.org/docs/0.12/debug/
###########################################################

import os
from pathlib import Path

import psutil
import click
from jinja2 import Environment, PackageLoader
from pywps import configuration

from . import wsgi
from urllib.parse import urlparse

PID_FILE = Path(__file__).parent.joinpath("pywps.pid").resolve()

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

template_env = Environment(
    loader=PackageLoader("{{ cookiecutter.project_slug }}", "templates"),
    autoescape=True,
)


def write_user_config(**kwargs) -> Path:
    r"""
    Write a custom configuration file.

    Parameters
    ----------
    **kwargs : dict
        Configuration parameters.

    Returns
    -------
    Path
        The path to the written configuration file.
    """
    config_templ = template_env.get_template("pywps.cfg")
    rendered_config = config_templ.render(**kwargs)
    config_file = Path(__file__).parent.joinpath(".custom.cfg").resolve()
    with config_file.open("w") as fp:
        fp.write(rendered_config)
    return config_file


def get_host() -> tuple[str, int]:
    """
    Gather host information.

    Returns
    -------
    tuple[str, int]
        The host and port.
    """
    url = configuration.get_config_value("server", "url")
    url = url or "http://localhost:{{ cookiecutter.http_port }}/wps"

    click.echo(f"starting WPS service on {url}")

    parsed_url = urlparse(url)
    if ":" in parsed_url.netloc:
        host, port = parsed_url.netloc.split(":")
        port = int(port)
    else:
        host = parsed_url.netloc
        port = 80
    return host, port


def run_process_action(action: str | None = None):
    """
    Run an action with psutil on current process and return a status message.

    Parameters
    ----------
    action : str, optional
        The action to perform, by default "status".
    """
    action = action or "status"
    try:
        with PID_FILE.open() as fp:
            pid = int(fp.read())
            p = psutil.Process(pid)
            if action == "stop":
                p.terminate()
                msg = f"pid={p.pid}, status=terminated"
            else:
                from psutil import _pprint_secs

                msg = f"pid={p.pid}, status={p.status()}, created={_pprint_secs(p.create_time())}"
        if action == "stop":
            PID_FILE.unlink()
    except OSError:
        msg = 'No PID file found. Service not running? Try "netstat -nlp | grep :5000".'
    except psutil.NoSuchProcess as e:
        msg = e.msg
    click.echo(msg)


def _run(application, bind_host=None, daemon=False):
    from werkzeug.serving import run_simple

    # call this *after* app is initialized ... needs pywps config.
    host, port = get_host()
    bind_host = bind_host or host
    # need to serve the wps outputs
    static_files = {"/outputs": configuration.get_config_value("server", "outputpath")}
    run_simple(
        hostname=bind_host,
        port=port,
        application=application,
        use_debugger=False,
        use_reloader=False,
        threaded=True,
        # processes=2,
        use_evalex=not daemon,
        static_files=static_files,
    )


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli():
    """
    Command line to start/stop a PyWPS service.

    Do not use this service in a production environment.
    It's intended to be running in a test environment only!
    For more documentation, visit https://pywps.org/doc
    """
    pass


@cli.command()
def status():
    """Show status of PyWPS service."""
    run_process_action(action="status")


@cli.command()
def stop():
    """Stop PyWPS service."""
    run_process_action(action="stop")


@cli.command()
@click.option("--config", "-c", metavar="PATH", help="path to pywps configuration file.")
@click.option("--bind-host", "-b", metavar="IP-ADDRESS", default="127.0.0.1", help="IP address used to bind service.")
@click.option("--daemon", "-d", is_flag=True, help="run in daemon mode.")
@click.option("--hostname", metavar="HOSTNAME", default="localhost", help="hostname in PyWPS configuration.")
@click.option("--port", metavar="PORT", default="5000", help="port in PyWPS configuration.")
@click.option("--maxsingleinputsize", default="200mb", help="maxsingleinputsize in PyWPS configuration.")
@click.option("--maxprocesses", metavar="INT", default="10", help="maxprocesses in PyWPS configuration.")
@click.option("--parallelprocesses", metavar="INT", default="2", help="parallelprocesses in PyWPS configuration.")
@click.option("--log-level", metavar="LEVEL", default="INFO", help="log level in PyWPS configuration.")
@click.option("--log-file", metavar="PATH", default="pywps.log", help="log file in PyWPS configuration.")
@click.option("--database", default="sqlite:///pywps-logs.sqlite", help="database in PyWPS configuration")
@click.option("--outputurl", default="", help="base URL for file downloads")
@click.option("--outputpath", default="", help="base directory where outputs are written")
def start(
    config,
    bind_host,
    daemon,
    hostname,
    port,
    maxsingleinputsize,
    maxprocesses,
    parallelprocesses,
    log_level,
    log_file,
    database,
    outputurl,
    outputpath,
):
    """
    Start PyWPS service.

    This service is by default available at http://localhost:{{ cookiecutter.http_port }}/wps

    Parameters
    ----------
    config : str
        Path to pywps configuration file.
    bind_host : str
        IP address used to bind service.
    daemon : bool
        Run in daemon mode.
    hostname : str
        Hostname in PyWPS configuration.
    port : str
        Port in PyWPS configuration.
    maxsingleinputsize : str
        Maxsingleinputsize in PyWPS configuration.
    maxprocesses : int
        Maxprocesses in PyWPS configuration.
    parallelprocesses : int
        Parallelprocesses in PyWPS configuration.
    log_level : str
        Log level in PyWPS configuration.
    log_file : str
        Log file in PyWPS configuration.
    database : str
        Database in PyWPS configuration.
    outputurl : str
        Base URL for file downloads.
    outputpath : str
        Base directory where outputs are written.
    """
    if PID_FILE.exists():
        click.echo(f'PID file exists: "{PID_FILE}". Service still running?')
        os._exit(0)
    cfgfiles = [
        write_user_config(
            wps_hostname=hostname,
            wps_port=port,
            wps_maxsingleinputsize=maxsingleinputsize,
            wps_maxprocesses=maxprocesses,
            wps_parallelprocesses=parallelprocesses,
            wps_log_level=log_level,
            wps_log_file=log_file,
            wps_database=database,
            wps_outputurl=outputurl,
            wps_outputpath=outputpath,
        )
    ]
    if config:
        cfgfiles.append(config)
    app = wsgi.create_app(cfgfiles)
    # let's start the service ...
    # See:
    # * https://github.com/geopython/pywps-flask/blob/master/demo.py
    # * http://werkzeug.pocoo.org/docs/0.14/serving/
    if daemon:
        # daemon (fork) mode
        pid = None
        try:
            pid = os.fork()
            if pid:
                click.echo(f"forked process id: {pid}")
                with PID_FILE.open("w") as fp:
                    fp.write(f"{pid}")
        except OSError as e:
            msg = f"{e.strerror} [{e.errno}]"
            raise Exception(msg)

        if pid == 0:
            os.setsid()
            _run(app, bind_host=bind_host, daemon=True)
        else:
            os._exit(0)
    else:
        # no daemon
        _run(app, bind_host=bind_host)
