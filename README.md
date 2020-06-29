# infotrem
Web application for railroads related media and information


## Setup

Copy the environment file template to the real env

```
cp backend/.env.template backend/.env
cp frontend/.env.template frontend/.env
```

Edit both files to your data.

Start the container (make sure that the `ngnix-proxy` container is running)
```
docker-compose up --build -d
```

And run the setup

 ```
 docker exec -it infotrem-api sh "/code/setup.sh"
```

It should be available at the URL:

```
http://api.infotrem.lan/
http://infotrem.lan/
```