#!/bin/sh

until cd /app/library_events_platform
do
    echo "Waiting for server volume..."
done

celery -A library_events_platform worker --loglevel=info --concurrency 1 -E