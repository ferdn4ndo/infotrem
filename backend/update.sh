#!/bin/bash

echo "WARNING: THIS PROCESS WILL UPDATE THE EXISTING CSCCONSULTORIA DATABASE!"
echo "THIS IS IRREVERSIBLE!"
echo "Database update countdown: 5s (press Ctrl+C to cancel)"
sleep 1s
echo "Database update countdown: 4s (press Ctrl+C to cancel)"
sleep 1s
echo "Database update countdown: 3s (press Ctrl+C to cancel)"
sleep 1s
echo "Database update countdown: 2s (press Ctrl+C to cancel)"
sleep 1s
echo "Database update countdown: 1s (press Ctrl+C to cancel)"
sleep 1s

echo "Updating DB.."

python manage.py makemigrations
python manage.py migrate
