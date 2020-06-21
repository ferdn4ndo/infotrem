#!/bin/sh

if [ "${ENV_MODE}" = "prod" ]; then
  echo "Starting in production mode..."
  yarn run build
  serve --host 0.0.0.0 -l 9906 -s dist
else
  echo "Starting in development mode..."
  cross-env BABEL_ENV=dev vue-cli-service serve --port=9906 --disable-host-check
fi
