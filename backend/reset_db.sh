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

echo "Reseting migrations"
#python manage.py flush --noinput
rm -f /code/api/migrations/*.py

echo "RESET COMPLETED!"
echo "Run setup.sh to install the database again"
exit 0
