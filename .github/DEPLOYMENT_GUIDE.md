# Deployment Guide

This document explains how deployment works in this repository.

## Two Deployment Options

### Option 1: Tag-based Deployment (Recommended)

This is the standard approach for Python packages:

1. **Make your changes** and commit them to the main branch
2. **Bump the version** when ready to release:
   ```bash
   python scripts/bump_version.py [patch|minor|major]
   ```
3. **Push the changes and tag**:
   ```bash
   git push
   git push origin v<new_version>
   ```
4. **Deployment automatically triggers** when the tag is pushed

### Option 2: Branch-based Deployment (Current Setup)

The deployment workflow is currently configured to deploy on every push to main:

1. **Make your changes** and commit them to the main branch
2. **Push to main** - deployment will trigger automatically
3. **Version check** - if the version already exists on PyPI, deployment will fail with helpful instructions

## How It Works

### CI Workflow (ci.yml)
- **Triggers**: Push to main/develop, pull requests
- **Purpose**: Run tests, linting, and formatting checks
- **Python versions**: Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12

### Deployment Workflow (deploy.yml)
- **Triggers**: 
  - Push to main branch (branch-based deployment)
  - Push to tags starting with 'v' (tag-based deployment)
  - Published releases
  - Manual trigger
- **Purpose**: Deploy the package to PyPI

## Version Management

The version is managed in `pyproject.toml`:
```toml
[project]
version = "0.1.7"
```

## Safety Checks

When deploying from main branch, the workflow:
1. Checks if the current version already exists on PyPI
2. If it exists, fails with instructions to bump the version
3. If it doesn't exist, proceeds with deployment

## Required Secrets

Make sure these secrets are set in your repository:
- `PYPI_API_TOKEN` - for production PyPI deployments
- `TEST_PYPI_API_TOKEN` - for test PyPI deployments (optional)

## Troubleshooting

### "Version already exists on PyPI"
If deployment fails because the version exists:
1. Bump the version: `python scripts/bump_version.py patch`
2. Push the changes: `git push`
3. Push the tag: `git push origin v<new_version>`

### "PYPI_API_TOKEN secret is not set"
1. Go to your repository settings
2. Navigate to Secrets and variables → Actions
3. Add the `PYPI_API_TOKEN` secret with your PyPI API token