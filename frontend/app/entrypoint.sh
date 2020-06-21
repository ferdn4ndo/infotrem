#!/bin/sh

if [ "${ENV_MODE}" = "prod" ]; then
  echo "Starting in production mode..."
  yarn run build
  serve --host 0.0.0.0 -l 9903 -s dist
else
  echo "Starting in development mode..."
  cross-env BABEL_ENV=dev vue-cli-service serve --port=9903 --disable-host-check
fi
