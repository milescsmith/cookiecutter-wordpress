FROM php:5.6-apache

RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

RUN echo PassEnv DATABASE_URL > /etc/apache2/conf-enabled/wp-env.conf

RUN echo "<?php" > /var/www/wp-constants.php
RUN echo "define('DB_URL', getenv('DATABASE_URL'));" >> /var/www/wp-constants.php
RUN echo "define('AUTH_KEY',         'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('SECURE_AUTH_KEY',  'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('LOGGED_IN_KEY',    'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('NONCE_KEY',        'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('AUTH_SALT',        'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('SECURE_AUTH_SALT', 'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('LOGGED_IN_SALT',   'abcdefg');" >> /var/www/wp-constants.php
RUN echo "define('NONCE_SALT',       'abcdefg');" >> /var/www/wp-constants.php
