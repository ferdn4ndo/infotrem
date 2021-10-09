#!/bin/sh

echo "-=- InfoTrem-App -=-"

if [ "$START_SERVER" = "true" ]
then
  if [ "$ENV_MODE" = "prod" ]
  then
    echo "Starting server in PRODUCTION mode"
    yarn run build && yarn run serve
  else
    echo "Starting server in DEVELOPMENT mode"
    yarn run dev
  fi
else
  echo "Starting dummy container zZzZz"
  tail -f /dev/null
fi
