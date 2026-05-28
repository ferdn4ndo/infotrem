# InfoTrem Root Agent Notes

## Repo Role

This repository is the integration and orchestration layer for InfoTrem. The
application code lives in git submodules:

- `infotrem-api`: Go/Gin API, PostgreSQL migrations, fixtures, API tests.
- `infotrem-web`: Vue/Vite frontend, Cypress and Vitest tests.

Root-level changes should focus on docs, local orchestration, integration smoke
tests, and raw data-ingestion source material.

## Submodule Workflow

- Initialize or refresh submodules with `make submodules`.
- Check submodule state before broad edits with `git submodule status` and
  `git -C <submodule> status --short --branch`.
- Make API implementation changes in `infotrem-api` and frontend changes in
  `infotrem-web`; do not duplicate app code at the root.
- Keep submodule commits and root commits conceptually separate when possible.
- Do not delete `.submodule-backups/`; it is ignored and may contain local
  safety backups from the migration to submodules.

## Local Development

- `make env` creates missing `.env` files from templates.
- `make api-up` starts `infotrem-api` and its local Postgres dependency.
- `make web-dev` starts Vite for `infotrem-web`.
- `make dev` starts the API path, waits for API health, then starts Vite.
- `make integration-smoke` checks the API, API docs, frontend URL, and Vite
  proxy path.

uServer Auth and uServer FileMgr are expected to be running outside this repo.
Configure their hosts and tokens in `infotrem-api/.env`.

## Production Assumptions

- `infotrem-web` builds static assets for an S3 static website bucket.
- `userver-spa-bucket-gateway` maps public hostnames to S3 website endpoints
  through `websites/*.json` and runs behind `userver-web`.
- `infotrem-api` runs as a container in the uServer ecosystem and exposes
  `GET /health` for health checks.

## Raw Source Data

Files under `_docs/_to_be_converted_to_fixtures/` are raw source material for
future ingestion. Treat them as immutable inputs. Create derived fixture files
elsewhere only after the ingestion format is defined.

## Verification

Use the narrowest meaningful checks:

```sh
make integration-smoke
make -C infotrem-api unit-test
yarn --cwd infotrem-web test
```

Run submodule-specific lint or integration tests when touching those areas.
Never commit generated folders such as `node_modules`, `dist`, `coverage`,
Go build outputs, local `.env` files, or Cypress screenshots/videos.
