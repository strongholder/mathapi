#!/bin/bash

gunicorn -w 1 -t 60 --threads 1 --log-config gunicorn_logging.conf --bind unix:/app/gunicorn.sock "mathapi:create_app()"&
sleep 3
echo "Starting nginx..."
nginx -g 'daemon off;'

