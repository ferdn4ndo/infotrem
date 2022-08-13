#!/bin/bash

# Check if the database exists
if PGPASSWORD=${POSTGRES_ROOT_PASS} psql -h "${POSTGRES_HOST}" -U "${POSTGRES_ROOT_USER}" -p "${POSTGRES_PORT}" -lqt | cut -d \| -f 1 | grep -qw "${POSTGRES_DB}"; then
    echo "Database checking passed successfully"
else
    echo "The database checking failed to find the database '${POSTGRES_DB}'. Running setup script..."
    ./setup.sh
fi

# Starts the server
if [ "${ENV_MODE}" == "prod" ]
then
  echo "Starting in production mode..."

  gunicorn --access-logfile /code/logs/access.log --worker-tmp-dir /dev/shm --workers ${GUVICORN_WORKERS} --bind 0.0.0.0:5000 api.wsgi
else
  echo "Starting in development mode..."

  python manage.py runserver 0.0.0.0:5000
fi
