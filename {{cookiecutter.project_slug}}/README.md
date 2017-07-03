# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}

## Quickstart

[Install Docker](https://www.docker.com/get-docker) for your development platform.

Bring up dev environment:

    cd dev/docker
    docker-compose up -d

Start and interactive shell inside the `devbox` container:

    docker exec -it {{ cookiecutter.project_slug }}_devbox bash

Install the packages:

    cd src
    make install

Verify that the website is up and running:

    curl http://localhost:9180
