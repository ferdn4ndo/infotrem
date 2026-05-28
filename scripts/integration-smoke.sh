#!/bin/sh
set -eu

API_URL="${API_URL:-http://localhost:8080}"
WEB_URL="${WEB_URL:-http://localhost:5173}"

check_url() {
  label="$1"
  url="$2"

  printf 'Checking %s: %s\n' "$label" "$url"
  curl -fsS --max-time 10 "$url" >/dev/null
}

check_url "API health" "$API_URL/health"
check_url "API OpenAPI document" "$API_URL/docs/swagger.json"
check_url "frontend" "$WEB_URL/"
check_url "frontend API proxy" "$WEB_URL/api/health"

echo "Integration smoke checks passed."
