#!/bin/sh

echo "-=- InfoTrem-App -=-"

if [ "$START_SERVER" = "true" ]
then
  if [ "$ENV_MODE" = "prod" ]
  then
    echo "Starting server in PRODUCTION mode"
    npm build
  else
    echo "Starting server in DEVELOPMENT mode"
    npm start
  fi
else
  echo "Starting dummy container zZzZz"
  tail -f /dev/null
fi
