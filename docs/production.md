# Production

## Frontend

`infotrem-web` is deployed as static assets:

1. Build the SPA in `infotrem-web`.
2. Upload the generated assets to an S3 bucket configured for static website
   hosting.
3. Configure `userver-spa-bucket-gateway` with a `websites/*.json` mapping.
4. Expose the gateway through `userver-web`.

The gateway expects each site definition to include:

```json
{
  "BUCKET_URL": "<bucket-name>.s3-website-<region>.amazonaws.com",
  "DOMAIN": "<public-domain>"
}
```

Set `VIRTUAL_HOST` in the gateway `.env` to the comma-separated hostnames that
`userver-web` should route to the gateway. TLS is handled by `userver-web`; the
gateway focuses on hostname to bucket mapping.

SPA routing depends on the bucket and gateway serving `index.html` for client
routes. Keep that behavior in mind when configuring the bucket error document
and gateway routing.

## Backend

`infotrem-api` is deployed as a container in the uServer ecosystem. The image
entrypoint runs database migrations and starts the API server.

Required production environment values include:

- `PORT`
- `ENVIRONMENT`
- `DATABASE_HOST`
- `DATABASE_PORT`
- `DATABASE_NAME`
- `DATABASE_USERNAME`
- `DATABASE_PASSWORD`
- `USERVER_AUTH_HOST`
- `USERVER_AUTH_SYSTEM_NAME`
- `USERVER_AUTH_SYSTEM_TOKEN`
- `USERVER_FILEMGR_HOST`

Optional values include `SENTRY_DSN` and cron-related configuration.

Expose `GET /health` through the container health check and outer routing. API
documentation is available at `/docs/swagger.json`, `/docs/swagger.yaml`, and
`/docs/openapi` when the service is running.

## Release Ownership

The root repository coordinates versions by submodule commit. Application
releases are built and tested in their owning repositories:

- Frontend build and static asset deployment: `infotrem-web`.
- Backend image build, migrations, and API tests: `infotrem-api`.
