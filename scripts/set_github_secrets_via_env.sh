#!/usr/bin/env bash
# Read environment variables and set them as GitHub repo secrets for the current repo
# Requires: gh CLI authenticated and inside repo directory
# Expects RENDER_API_KEY, RENDER_WEB_SERVICE_ID, RENDER_WORKER_SERVICE_ID present in environment

set -euo pipefail

for name in RENDER_API_KEY RENDER_WEB_SERVICE_ID RENDER_WORKER_SERVICE_ID; do
  if [ -z "${!name:-}" ]; then
    echo "Environment variable $name is not set. Aborting."
    exit 1
  fi
  echo "Setting GitHub secret $name..."
  gh secret set "$name" --body "${!name}"
done

echo "Secrets set."
