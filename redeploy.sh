#!/bin/sh

if [ -z "$RUN_ENV" ]; then
    echo 'Please set up RUN_ENV variable'
    exit 1
fi

if [ "$RUN_ENV" = "PROD" ]; then
    sudo git pull
fi


docker-compose stop
docker-compose rm -f

if [ "$1" = stop ]; then
	exit 1
fi
docker-compose up -d