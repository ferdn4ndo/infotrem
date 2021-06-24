#!/bin/bash

python manage.py makemigrations api
python manage.py migrate api

echo "Migrating..."
python manage.py migrate --run-syncdb

# Import of data fixtures
echo "Importing Event fixture..."
python manage.py loaddata /code/api/fixtures/event_fixture.yaml
echo "Importing EventVacancyType fixture..."
python manage.py loaddata /code/api/fixtures/event_vacancy_type_fixture.yaml
echo "Importing EventVacancy fixture..."
python manage.py loaddata /code/api/fixtures/event_vacancy_fixture.yaml
#echo "Importing User fixture..."
#python manage.py loaddata /code/api/fixtures/custom_user_fixture.yaml

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

echo "Updating IBGE states and cities"
python manage.py update_locations_from_ibge

echo "SETUP COMPLETED!"
exit 0
