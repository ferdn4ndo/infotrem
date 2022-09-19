#!/bin/bash

echo "WARNING: THIS PROCESS WILL DESTROY ANY EXISTING INFOTREM DATABASE!"
echo "THIS IS IRREVERSIBLE!"
echo "Database destroy countdown: 5s (press Ctrl+C to cancel)"
sleep 1s
echo "Database destroy countdown: 4s (press Ctrl+C to cancel)"
sleep 1s
echo "Database destroy countdown: 3s (press Ctrl+C to cancel)"
sleep 1s
echo "Database destroy countdown: 2s (press Ctrl+C to cancel)"
sleep 1s
echo "Database destroy countdown: 1s (press Ctrl+C to cancel)"
sleep 1s

echo "Reseting DB..."

PGPASSWORD=${POSTGRES_ROOT_PASS} psql -h "${POSTGRES_HOST}" -U "${POSTGRES_ROOT_USER}" -p "${POSTGRES_PORT}" <<EOF
  REVOKE CONNECT ON DATABASE ${POSTGRES_DB} FROM public;

  SELECT pid, pg_terminate_backend(pid)
  FROM pg_stat_activity
  WHERE pg_stat_activity.datname = '${POSTGRES_DB}' AND pid <> pg_backend_pid();

  DROP DATABASE IF EXISTS ${POSTGRES_DB};
  CREATE DATABASE ${POSTGRES_DB};

  GRANT CONNECT ON DATABASE ${POSTGRES_DB} TO public;

  DROP OWNED BY ${POSTGRES_USER};
  DROP USER IF EXISTS ${POSTGRES_USER};
  CREATE USER ${POSTGRES_USER} WITH ENCRYPTED PASSWORD '${POSTGRES_PASS}';

  REVOKE ALL PRIVILEGES ON DATABASE postgres FROM ${POSTGRES_USER};
  ALTER USER ${POSTGRES_USER} CREATEDB;
  GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};
\gexec
EOF

echo "Reseting API migrations"
python manage.py makemigrations api
python manage.py migrate api

echo "Reseting Core migrations"
python manage.py makemigrations core
python manage.py migrate core

echo "Migrating..."
python manage.py migrate --run-syncdb

# Import of data fixtures
echo "Importing User fixture..."
python manage.py loaddata /code/core/fixtures/user_fixture.yaml

# Import of data fixtures
echo "Importing Company fixture..."
python manage.py loaddata /code/core/fixtures/company_fixture.yaml

echo "Importing Track Gauge fixture..."
python manage.py loaddata /code/core/fixtures/track_gauge_fixture.yaml

echo "Importing Manufacturer fixture..."
python manage.py loaddata /code/core/fixtures/manufacturer_fixture.yaml

echo "Importing Rolling Stock fixture..."
python manage.py loaddata /code/core/fixtures/rolling_stock_fixture.yaml

echo "Importing Freight Car Category fixture..."
python manage.py loaddata /code/core/fixtures/freight_car_category_fixture.yaml

echo "Importing Freight Car Type fixture..."
python manage.py loaddata /code/core/fixtures/freight_car_type_fixture.yaml

echo "Importing Freight Car Gross Weight Type fixture..."
python manage.py loaddata /code/core/fixtures/freight_car_gross_weight_type_fixture.yaml

echo "Importing Locomotive Design fixture..."
python manage.py loaddata /code/core/fixtures/locomotive_design_fixture.yaml

echo "Importing Locomotive fixture..."
python manage.py loaddata /code/core/fixtures/locomotive_fixture.yaml

echo "Importing Non Revenue Car Type fixture..."
python manage.py loaddata /code/core/fixtures/non_revenue_car_type_fixture.yaml

echo "Importing Passenger Car Type fixture..."
python manage.py loaddata /code/core/fixtures/passenger_car_type_fixture.yaml

echo "Importing Passenger Car Material fixture..."
python manage.py loaddata /code/core/fixtures/passenger_car_material_fixture.yaml

echo "Importing Location State fixture..."
python manage.py loaddata /code/core/fixtures/location_state_fixture.yaml

echo "Importing Location City fixture..."
python manage.py loaddata /code/core/fixtures/location_city_fixture.yaml

echo "Importing Location fixture..."
python manage.py loaddata /code/core/fixtures/location_fixture.yaml

echo "Importing Path fixture..."
python manage.py loaddata /code/core/fixtures/path_fixture.yaml

echo "Importing Path Point fixture..."
python manage.py loaddata /code/core/fixtures/path_point_fixture.yaml

echo "Importing Location Path fixture..."
python manage.py loaddata /code/core/fixtures/location_path_fixture.yaml

echo "Importing Route fixture..."
python manage.py loaddata /code/core/fixtures/route_fixture.yaml

echo "Importing Route Section fixture..."
python manage.py loaddata /code/core/fixtures/route_section_fixture.yaml

echo "Importing Information fixture..."
python manage.py loaddata /code/core/fixtures/information_fixture.yaml

echo "Importing Sigo Series Information fixture..."
python manage.py loaddata /code/core/fixtures/sigo_series_information_fixture.yaml

echo "Importing Sigo Regional fixture..."
python manage.py loaddata /code/core/fixtures/sigo_regional_fixture.yaml

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Creating auth system"

system_resp=$(
  curl -sS -X POST "http://${USERVER_AUTH_HOST}/auth/system" \
    -H "Authorization: Token ${USERVER_AUTH_SYSTEM_CREATION_TOKEN}" \
    -H "Content-Type: application/json" \
    --data @- <<END
{
  "name": "${USERVER_AUTH_SYSTEM_NAME}",
  "token": "${USERVER_AUTH_SYSTEM_TOKEN}"
}
END
)
echo "System response:"
echo "${system_resp}"

echo "Creating auth user"

reg_resp=$(
  curl -sS -X POST "http://${USERVER_AUTH_HOST}/auth/register" \
    -H "Content-Type: application/json" \
    --data @- <<END
{
  "username": "${USERVER_AUTH_USER}",
  "system_name": "${USERVER_AUTH_SYSTEM_NAME}",
  "system_token": "${USERVER_AUTH_SYSTEM_TOKEN}",
  "password": "${USERVER_AUTH_PASSWORD}",
  "is_admin": true
}
END
)

echo "Register response:"
echo "${reg_resp}"

login_resp=$(
  curl -sS -X POST "http://${USERVER_AUTH_HOST}/auth/login" \
    -H "Content-Type: application/json" \
    --data @- <<END
{
  "username": "${USERVER_AUTH_USER}",
  "system_name": "${USERVER_AUTH_SYSTEM_NAME}",
  "system_token": "${USERVER_AUTH_SYSTEM_TOKEN}",
  "password": "${USERVER_AUTH_PASSWORD}"
}
END
)

echo "Login response:"
echo "${login_resp}"

echo "Creating superuser"
#export DJANGO_SUPERUSER_PASSWORD=${USERVER_AUTH_PASSWORD}
python manage.py createsuperuser --noinput --id="${DJANGO_SUPERUSER_ID}"

echo "SETUP COMPLETED!"
exit 0
