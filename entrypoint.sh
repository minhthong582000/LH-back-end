#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

echo "Flush any previous unsaved manage.py command"
python manage.py flush --no-input

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create super user for admin page
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    echo "Create Superuser: $DJANGO_SUPERUSER_USERNAME"
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000