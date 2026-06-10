\# GitHub Actions Enterprise CI/CD Demo.



A demonstration project showcasing an enterprise-grade GitHub Actions pipeline for building, testing, securing, publishing, and deploying a containerized FastAPI application to Azure Container Apps.



\## Overview



This project demonstrates modern DevOps and platform engineering practices including:



\- Automated testing

\- Multi-version validation

\- Dependency review

\- Container image creation

\- Container vulnerability scanning

\- SBOM generation

\- GitHub Container Registry publishing

\- Azure OIDC authentication

\- Automated deployment to Development

\- Manual approval before Production deployment

\- Production deployment validation



\## Technology Stack



\### Application



\- Python 3

\- FastAPI

\- Uvicorn

\- Pytest



\### CI/CD



\- GitHub Actions

\- GitHub Container Registry (GHCR)



\### Security



\- Trivy Container Scanning

\- CycloneDX SBOM Generation

\- Dependency Review

\- OIDC Federated Authentication



\### Cloud



\- Azure Container Apps

\- Azure Managed Environment

\- Azure Log Analytics



\---



\# Pipeline Architecture



```text

Developer Push

&#x20;       │

&#x20;       ▼

Quality Gates

&#x20; ├─ Ruff Linting

&#x20; ├─ Unit Tests

&#x20; ├─ Coverage Validation

&#x20; └─ Matrix Testing

&#x20;       │

&#x20;       ▼

Dependency Review

&#x20;       │

&#x20;       ▼

Docker Build

&#x20;       │

&#x20;       ▼

Container Smoke Test

&#x20;       │

&#x20;       ▼

Trivy Security Scan

&#x20;       │

&#x20;       ▼

SBOM Generation

&#x20;       │

&#x20;       ▼

Publish Image to GHCR

&#x20;       │

&#x20;       ▼

Deploy DEV

&#x20;       │

&#x20;       ▼

DEV Smoke Test

&#x20;       │

&#x20;       ▼

Manual Approval

&#x20;       │

&#x20;       ▼

Deploy PROD

&#x20;       │

&#x20;       ▼

PROD Smoke Test

```



\---



\# Quality Controls



\## Matrix Testing



The application is validated against multiple Python versions:



\- Python 3.11

\- Python 3.12

\- Python 3.13



\## Linting



Code quality is validated using Ruff.



\## Test Coverage



Pytest coverage enforcement ensures a minimum quality threshold before deployment.



\---



\# Security Controls



\## Dependency Review



Pull requests are automatically evaluated for vulnerable dependency changes.



\## Container Vulnerability Scanning



Trivy scans the generated Docker image for:



\- Critical vulnerabilities

\- High vulnerabilities



\## Software Bill of Materials (SBOM)



A CycloneDX SBOM is generated and published as a build artifact.



\## Secretless Azure Authentication



GitHub Actions authenticates to Azure using OpenID Connect (OIDC).



No Azure client secrets are stored within GitHub.



\---



\# Container Registry



Docker images are published to GitHub Container Registry:



```text

ghcr.io/<github-user>/github-actions-demo

```



Images are tagged with:



```text

latest

<git-commit-sha>

```



This provides immutable deployment versions.



\---



\# Azure Deployment



\## Development



Automatic deployment after successful validation.



Environment:



```text

dev

```



\## Production



Production deployment requires manual approval using GitHub Environments.



Environment:



```text

prod

```



This demonstrates release governance and separation of duties.



\---



\# Running Locally



\## Create Virtual Environment



```bash

python -m venv .venv

```



\### Windows



```bash

.venv\\Scripts\\activate.bat

```



\### PowerShell



```powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

. .\\.venv\\Scripts\\Activate.ps1

```



\## Install Dependencies



```bash

pip install -r requirements.txt

```



\## Run Application



```bash

uvicorn app.main:app --reload

```



Application:



```text

http://localhost:8000

```



Swagger:



```text

http://localhost:8000/docs

```



Health Check:



```text

http://localhost:8000/health

```



\---



\# Running Tests



```bash

python -m pytest

```



Coverage:



```bash

python -m pytest --cov=app --cov-report=term-missing

```



\---



\# Docker



Build:



```bash

docker build -t github-actions-demo .

```



Run:



```bash

docker run -p 8000:8000 github-actions-demo

```



\---



\# Key Architecture Concepts Demonstrated



\- CI/CD Automation

\- Shift Left Security

\- Supply Chain Security

\- Containerization

\- Immutable Deployments

\- OIDC Federation

\- Environment Promotion

\- Release Governance

\- Infrastructure as Code Readiness

\- Cloud-Native Deployment Patterns



\---



\# Future Enhancements



\- Terraform Infrastructure Validation

\- Image Signing (Cosign)

\- Provenance Attestation

\- Automated Rollback Workflow

\- Performance Testing

\- ChatOps Integration

\- Reusable GitHub Action Workflows

