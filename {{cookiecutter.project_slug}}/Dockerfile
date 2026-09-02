{%- set license_spdx_codes = {
    'MIT license': 'MIT',
    'BSD license': 'BSD-3-Clause',
    'ISC license': 'ISC',
    'Apache Software License 2.0': 'Apache-2.0',
    'GNU General Public License v3': 'GPL-3.0-or-later'
} -%}
# vim:set ft=dockerfile:
FROM condaforge/miniforge3:26.5.3-0
ARG DEBIAN_FRONTEND=noninteractive
ENV PIP_ROOT_USER_ACTION=ignore
LABEL org.opencontainers.image.authors="Birdhouse"
LABEL org.opencontainers.image.created="2000-01-02T03:04:05Z"
LABEL org.opencontainers.image.description="{{ cookiecutter.project_name }} WPS"
{%- if cookiecutter.open_source_license in license_spdx_codes %}
LABEL org.opencontainers.image.licenses="{{ license_spdx_codes[cookiecutter.open_source_license] }}"
{%- endif %}
LABEL org.opencontainers.image.source="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}"
LABEL org.opencontainers.image.title="{{ cookiecutter.project_name }}WPS"
LABEL org.opencontainers.image.vendor="Birdhouse"
LABEL org.opencontainers.image.version="{{ cookiecutter.version }}"

# Set the working directory to /code
WORKDIR /code

# Create conda environment
COPY environment.yml .
RUN conda env create -n {{ cookiecutter.project_name }} -f environment.yml && \
    conda install -n {{ cookiecutter.project_name }} gunicorn && \
    conda clean --all --yes

# Add the project conda environment to the path
ENV PATH="/opt/conda/envs/{{ cookiecutter.project_name }}/bin:$PATH"

# Copy WPS project
COPY . /code

# Install WPS project
RUN pip install . --no-deps

# Start WPS service on port {{ cookiecutter.http_port }} on 0.0.0.0
EXPOSE {{ cookiecutter.http_port }}

CMD ["gunicorn", "--bind=0.0.0.0:{{ cookiecutter.http_port }}", "{{ cookiecutter.project_slug }}.wsgi:application"]

# docker build -t {{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }} .
# docker run -p {{ cookiecutter.http_port }}:{{ cookiecutter.http_port }} {{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}
# http://localhost:{{ cookiecutter.http_port }}/wps?request=GetCapabilities&service=WPS
# http://localhost:{{ cookiecutter.http_port }}/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0
