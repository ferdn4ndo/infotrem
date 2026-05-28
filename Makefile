SHELL := /bin/sh

API_DIR := infotrem-api
WEB_DIR := infotrem-web
API_URL ?= http://localhost:8080
WEB_URL ?= http://localhost:5173

.PHONY: submodules env api-up api-down api-logs web-install web-dev dev integration-smoke

submodules:
	git submodule update --init --recursive

env:
	./scripts/setup-env.sh

api-up:
	docker compose -f $(API_DIR)/docker-compose.yml up -d --build

api-down:
	docker compose -f $(API_DIR)/docker-compose.yml down

api-logs:
	docker compose -f $(API_DIR)/docker-compose.yml logs -f infotrem-api

web-install:
	yarn --cwd $(WEB_DIR) install

web-dev:
	yarn --cwd $(WEB_DIR) dev --host 0.0.0.0

dev: api-up
	./scripts/wait-url.sh "$(API_URL)/health"
	$(MAKE) web-dev

integration-smoke:
	API_URL="$(API_URL)" WEB_URL="$(WEB_URL)" ./scripts/integration-smoke.sh
