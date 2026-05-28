#!/bin/sh
set -eu

copy_if_missing() {
  src="$1"
  dest="$2"

  if [ ! -f "$src" ]; then
    echo "Missing template: $src" >&2
    return 1
  fi

  if [ -f "$dest" ]; then
    echo "Keeping existing $dest"
    return 0
  fi

  cp "$src" "$dest"
  echo "Created $dest from $src"
}

copy_if_missing "infotrem-api/.env.template" "infotrem-api/.env"
copy_if_missing "infotrem-web/.env.template" "infotrem-web/.env"

echo "Review infotrem-api/.env for local uServer Auth and FileMgr settings."
