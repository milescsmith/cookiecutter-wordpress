FROM python:3.6

RUN apt-get update && apt-get -y install curl wget sudo vim iputils-ping && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install cookiecutter

CMD ["/bin/ping", "-i 360", "localhost"]
