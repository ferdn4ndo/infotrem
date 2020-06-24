#!/bin/sh

echo "Reseting DB..."

query="select 'drop table \"' || tablename || '\" cascade;' from pg_tables where schemaname='public'"
params="-h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -U ${POSTGRES_USER} -d ${POSTGRES_DB}"

export PGPASSWORD="${POSTGRES_PASS}"
psql $params -t -c "${query}" | psql $params > /dev/null 2>& 1

echo "Reseting migrations"
#python manage.py flush --noinput
rm -f ./infotrem/migrations/*.py

python manage.py migrate auth

#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('${DJANGO_ADMIN_USER}', '${DJANGO_ADMIN_EMAIL}', '${DJANGO_ADMIN_PASSWORD}')"

echo "Migrating..."
python manage.py migrate --run-syncdb

echo "Creating super user..."

echo "Applying setup setps..."
cd /code/setup/ || exit 1

files=$(find . .py -type f 2>/dev/null | grep -E -e "/[0-9]{2}[0-9a-zA-Z_-]*.py" | sort -n)
for file in $files; do
  echo -e "\nRunning setup file ${file}..."
  python /code/manage.py shell < "${file}"
done

echo "SETUP COMPLETED!"
exit 0
