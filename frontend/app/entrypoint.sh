#!/bin/sh

if [ "${ENV_MODE}" = "production" ]; then
  echo "Starting in production mode..."
  yarn run build
  yarn run prod
else
  echo "Starting in development mode..."
  yarn run dev
fi
