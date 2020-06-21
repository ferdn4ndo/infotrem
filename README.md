# infotrem
Web application for railroads related media and information


## Setup

Enter the docker container using ```docker exec -it infotrem-api sh```

Then run the following commands:

```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

And then access the URL:

```
http://localhost:8000/setup-db
```