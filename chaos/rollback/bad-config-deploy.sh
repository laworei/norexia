#!/usr/bin/env bash
# Rollback: restore the baseline Compose configuration.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
docker compose -f "$ROOT/platform/compose.yaml" up -d --build --force-recreate snapshotd
echo "rolled back: bad-config-deploy"
