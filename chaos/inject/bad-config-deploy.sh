#!/usr/bin/env bash
# Inject: a "config deploy" sets the snapshot worker count to 0. The service stays healthy but jobs never run.
# Usage: chaos/inject/bad-config-deploy.sh   (local Docker Compose only)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
docker compose -f "$ROOT/platform/compose.yaml" -f "$ROOT/chaos/overrides/bad-config-deploy.yaml" up -d --build snapshotd
echo "injected: bad-config-deploy (details are sealed)"
