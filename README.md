# InfoTrem

InfoTrem is the coordination repository for the railroads media and information
application. Runtime code lives in two submodules:

- `infotrem-web`: Vue 3 + Vite single-page frontend.
- `infotrem-api`: Go + Gin API backed by PostgreSQL and uServer services.

The root repository owns integration documentation, local orchestration scripts,
and future data-ingestion source material under `_docs/`.

## Quick Start

Initialize submodules and create local environment files:

```sh
make submodules
make env
```

Start the backend stack for local development:

```sh
make api-up
```

Start the frontend development server:

```sh
make web-dev
```

Run a local smoke check:

```sh
make integration-smoke
```

The default local URLs are:

- Frontend: `http://localhost:5173`
- API: `http://localhost:8080`
- API health: `http://localhost:8080/health`
- API docs: `http://localhost:8080/docs/swagger.json`

## uServer Assumptions

Local development assumes the required uServer containers, especially
uServer Auth and uServer FileMgr, are already running and reachable from the
API through values in `infotrem-api/.env`.

Production serves `infotrem-web` as static assets from an S3 website bucket
behind `userver-spa-bucket-gateway`. The API is exposed as a container in the
uServer ecosystem.

## Documentation

- `docs/architecture.md`: repository and runtime architecture.
- `docs/development.md`: local setup and development workflow.
- `docs/integration-testing.md`: smoke checks and test boundaries.
- `docs/production.md`: production deployment contracts.
- `docs/data-ingestion.md`: raw source files and future fixture ingestion.
- `docs/frontend-backend-parity.md`: cross-repo backend-to-frontend feature roadmap.

Submodule-specific guidance remains in:

- `infotrem-api/README.md` and `infotrem-api/AGENTS.md`
- `infotrem-web/README.md` and `infotrem-web/AGENTS.md`