## Deploy & GitHub Actions notes

This repository includes a GitHub Actions workflow `.github/workflows/render-deploy.yml`
that triggers Render deployments by calling the Render API. To make it work you must
create three repository secrets in GitHub:

- RENDER_API_KEY : Your Render API key (with deploy permission)
- RENDER_WEB_SERVICE_ID : Render service ID for the web service
- RENDER_WORKER_SERVICE_ID : Render service ID for the worker service

You can obtain service IDs from the Render dashboard (Service settings -> Service ID).

Alternatively, connect the repository to Render via the Render dashboard to enable auto-deploys.
