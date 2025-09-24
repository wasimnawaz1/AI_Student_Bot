#!/usr/bin/env bash
# Usage: ./create_and_push.sh <github-username> <repo-name>
set -euo pipefail
GH_USER="$1"
REPO="$2"

git init
git add .
git commit -m "Initial commit: AI student bot"
git branch -M main

if command -v gh >/dev/null 2>&1; then
  gh repo create "${GH_USER}/${REPO}" --public --source=. --remote=origin --push
  echo "Repository created and pushed via gh."
else
  echo "gh CLI not found. Please create a repo on GitHub and then run:"
  echo "git remote add origin git@github.com:${GH_USER}/${REPO}.git"
  echo "git push -u origin main"
fi

echo "To set Render secrets in GitHub repo (recommended), run:"
echo "  gh secret set RENDER_API_KEY --body "<your-render-api-key>""
echo "  gh secret set RENDER_WEB_SERVICE_ID --body "<render-web-service-id>""
echo "  gh secret set RENDER_WORKER_SERVICE_ID --body "<render-worker-service-id>""
