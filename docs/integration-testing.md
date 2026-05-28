# Integration Testing

## Smoke Test

Run the root smoke check after starting the API and frontend:

```sh
make integration-smoke
```

The script checks:

- `GET http://localhost:8080/health`
- `GET http://localhost:8080/docs/swagger.json`
- `GET http://localhost:5173/`
- `GET http://localhost:5173/api/health`

The last request verifies that the Vite development proxy can reach the API.

You can override URLs when ports differ:

```sh
API_URL=http://localhost:18080 WEB_URL=http://localhost:4173 make integration-smoke
```

## Frontend E2E

`infotrem-web` contains Cypress tests. The integration smoke spec visits the app
and checks API health through the frontend base URL.

Run Cypress against the Vite preview server:

```sh
yarn --cwd infotrem-web build
yarn --cwd infotrem-web test:e2e
```

Run Cypress against a development server:

```sh
yarn --cwd infotrem-web test:e2e:dev
```

## Backend Tests

Use the backend test targets for API behavior:

```sh
make -C infotrem-api unit-test
make -C infotrem-api integration-test
make -C infotrem-api db-smoke
```

`integration-test` needs database environment variables. `db-smoke` exercises
migration, fixture, and search behavior against the configured test database.

## Test Boundaries

Root smoke tests should stay shallow and fast. Detailed behavior belongs in the
owning submodule:

- UI behavior and browser flows in `infotrem-web`.
- API handlers, services, migrations, and fixture loading in `infotrem-api`.
