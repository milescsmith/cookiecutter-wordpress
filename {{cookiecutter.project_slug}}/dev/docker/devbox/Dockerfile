FROM php:7.1-cli

RUN apt-get update && apt-get -y install curl git iputils-ping ncftp sudo unzip vim wget && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin

CMD ["/bin/ping", "-i 360", "localhost"]
