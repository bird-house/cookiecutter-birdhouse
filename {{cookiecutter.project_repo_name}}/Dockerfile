# vim:set ft=dockerfile:
FROM continuumio/miniconda3
MAINTAINER https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}
LABEL Description="{{ cookiecutter.project_name }} WPS" Vendor="Birdhouse" Version="{{ cookiecutter.version }}"

# Update Debian system
RUN apt-get update && apt-get install -y \
 build-essential \
&& rm -rf /var/lib/apt/lists/*

# Update conda
RUN conda update -n base conda

# Copy WPS project
COPY . /opt/wps

WORKDIR /opt/wps

# Create conda environment with PyWPS
RUN ["conda", "env", "create", "-n", "wps", "-f", "environment.yml"]

# Install WPS
RUN ["/bin/bash", "-c", "source activate wps && pip install -e ."]

# Start WPS service on port {{ cookiecutter.http_port }} on 0.0.0.0
EXPOSE {{ cookiecutter.http_port }}
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["source activate wps && exec {{ cookiecutter.project_slug }} start -b 0.0.0.0 -c /opt/wps/etc/demo.cfg"]

# docker build -t {{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }} .
# docker run -p {{ cookiecutter.http_port }}:{{ cookiecutter.http_port }} {{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}
# http://localhost:{{ cookiecutter.http_port }}/wps?request=GetCapabilities&service=WPS
# http://localhost:{{ cookiecutter.http_port }}/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0
