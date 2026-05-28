# Development

## Requirements

- Git with submodule support.
- Docker and Docker Compose v2.
- Go version required by `infotrem-api/go.mod`.
- Node.js `>=26 <27` and Yarn 1.x for `infotrem-web`.
- Running uServer Auth and uServer FileMgr containers.

## Bootstrap

Initialize or update the app submodules:

```sh
make submodules
```

Create missing local env files:

```sh
make env
```

Review `infotrem-api/.env` and set the uServer values for your local setup:

- `USERVER_AUTH_HOST`
- `USERVER_AUTH_SYSTEM_NAME`
- `USERVER_AUTH_SYSTEM_TOKEN`
- `USERVER_FILEMGR_HOST`

The frontend template defaults to:

```sh
VITE_INFOTREM_API_BASE_URL=http://localhost:8080
```

## Running Locally

Start the API and its local Postgres service:

```sh
make api-up
```

Start Vite:

```sh
make web-dev
```

Or run both with:

```sh
make dev
```

Default local URLs:

- Frontend: `http://localhost:5173`
- API: `http://localhost:8080`
- Vite API proxy: `http://localhost:5173/api/health`

## Submodule Commands

Backend commands are run inside `infotrem-api`:

```sh
make -C infotrem-api unit-test
make -C infotrem-api integration-test
make -C infotrem-api db-smoke
```

Frontend commands are run inside `infotrem-web`:

```sh
yarn --cwd infotrem-web install
yarn --cwd infotrem-web dev
yarn --cwd infotrem-web test
yarn --cwd infotrem-web lint
```

Use submodule-specific `README.md` and `AGENTS.md` files for detailed coding
guidance.
