ARG COMPOSER_VERSION="2.7.6"
ARG PHP_VERSION="8.2.19"

FROM composer:${COMPOSER_VERSION} AS composer
FROM public.ecr.aws/r7q2p6e2/gossm:0.3.0 AS gossm

FROM php:${PHP_VERSION}-apache-bullseye AS base

ARG DATADOG_TRACE_VERSION="0.86.0"
ARG APCU_VERSION="5.1.22"

# Global system packages should be installed here
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends unzip libzip4 && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

# Extensions and their build dependancies should installed here and cleaned up after docker-php-ext-install is done.
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends zlib1g-dev libxml2-dev libzip-dev libcurl4-openssl-dev && \
    pecl install apcu-${APCU_VERSION} datadog_trace-${DATADOG_TRACE_VERSION} && \
    docker-php-ext-install -j$(nproc) pdo pdo_mysql zip pcntl intl bcmath sockets && \
    docker-php-ext-enable apcu ddtrace opcache && \
    a2enmod rewrite && \
    apt-get -y purge zlib1g-dev libxml2-dev libzip-dev libcurl4-openssl-dev && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*
