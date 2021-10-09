# InfoTrem SPA

This is the container that holds the frontend SPA for InfoTrem.

This project requires  [userver-filemgr](https://github.com/ferdn4ndo/userver-filemgr) running to act as the microservice responsible for handling files and [userver-web](https://github.com/ferdn4ndo/userver-web) to run as the web server with reverse proxy.

## Getting Started

To run this container (along with the backend one), simply run:

```shell
docker-compose up
```

You can force the build (in case `package.json` was changed, for example) by running:

```shell
docker-compose up --build
```

**IMPORTANT**: Make sure your `.env` file is present before running. To create it, check the next section.

## Configuration

To configure the `infotrem-app` container, copy `.env.template` to `.env` and edit it as you wish.

The available parameters are:

* ***VIRTUAL_HOST***
  * **Description**: Defines the hostname to be used in the reverse proxy (running in [userver-web](https://github.com/ferdn4ndo/userver-web)).
  * **Default**: [empty]
  * **Required**: Yes if running behind a reverse proxy.


* ***LETSENCRYPT_HOST***
  * **Description**: Defines the HTTPS hostname to be used in the reverse proxy (running in [userver-web](https://github.com/ferdn4ndo/userver-web)).
  * **Default**: [empty]
  * **Required**: Yes if running behind a secured (HTTPS) reverse proxy.


* ***LETSENCRYPT_EMAIL***
  * **Description**: Defines the HTTPS e-mail (for the [Let's Encrypt](https://letsencrypt.org/) notifications) to be used in the reverse proxy (running in [userver-web](https://github.com/ferdn4ndo/userver-web)).
  * **Default**: [empty]
  * **Required**: Yes if running behind a secured (HTTPS) reverse proxy.


* ***START_SERVER***
  * **Description**: Determines if the `vite` server should be started at the entrypoint (`START_SERVER=true`) or if the container should hang online running `tail -f /dev/null` as the main command (`START_SERVER=false`)
  * **Default**: `true`
  * **Required**: No, but will be considered `false` if not present.


* ***ENV_MODE***
  * **Description**: Determines the environment to start the application (either `dev` or `prod`).
  * **Default**: `dev`
  * **Required**: Yes.


* ***VUE_APP_API_URL***
  * **Description**: Determines the base URL of the InfoTrem backend container.
  * **Default**: `http://localhost:5000/`
  * **Required**: Yes.


* ***VUE_APP_USERVER_FILEMGR_BASE_URL***
  * **Description**: Determines the base URL of the [userver-filemgr](https://github.com/ferdn4ndo/userver-filemgr) microservice.
  * **Default**: `http://filemgr.sd40.lan`
  * **Required**: Yes.


* ***VUE_APP_USERVER_FILEMGR_STORAGE_ID***
  * **Description**: Determines the ID of the storage to be used by the InfoTrem SPA inside the [userver-filemgr](https://github.com/ferdn4ndo/userver-filemgr) microservice.
  * **Default**: `[empty]`
  * **Required**: Yes.

## Contributions, Issues and Feedbacks

Feel free to create an issue in the repository to ask for help with issues or change requests. 

You will be very welcomed to create a PR with the changes you are suggesting too!

## License

[MIT](https://opensource.org/licenses/MIT)