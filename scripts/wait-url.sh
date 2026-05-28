#!/bin/sh
set -eu

url="${1:-}"
timeout_seconds="${WAIT_URL_TIMEOUT_SECONDS:-60}"

if [ -z "$url" ]; then
  echo "Usage: $0 <url>" >&2
  exit 2
fi

deadline=$(( $(date +%s) + timeout_seconds ))

while [ "$(date +%s)" -le "$deadline" ]; do
  if curl -fsS --max-time 5 "$url" >/dev/null; then
    echo "Ready: $url"
    exit 0
  fi
  sleep 2
done

echo "Timed out waiting for $url after ${timeout_seconds}s" >&2
exit 1
