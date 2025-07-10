# GitHub Actions Setup Guide

This repository includes several GitHub Actions workflows to automate testing, releasing, and deploying your Python package to PyPI.

## 📋 Workflows Overview

### 1. **CI Workflow** (`ci.yml`)
- **Triggers**: Push to `main`/`develop` branches, Pull Requests
- **Purpose**: Continuous Integration testing
- **Actions**:
  - Tests across Python 3.7-3.12
  - Code linting with flake8
  - Code formatting check with black
  - Security scanning with safety and bandit
  - Code coverage reporting

### 2. **Deploy Workflow** (`deploy.yml`)
- **Triggers**: 
  - Push to version tags (e.g., `v0.1.4`)
  - GitHub releases
  - Manual workflow dispatch
- **Purpose**: Automated deployment to PyPI
- **Actions**:
  - Runs tests first
  - Builds the package
  - Publishes to Test PyPI (manual trigger) or PyPI (tags/releases)

### 3. **Release Workflow** (`release.yml`)
- **Triggers**: 
  - Push to `main` branch when `pyproject.toml` version changes
  - Manual workflow dispatch with version bump options
- **Purpose**: Automated GitHub release creation
- **Actions**:
  - Detects version changes
  - Creates GitHub releases with changelogs
  - Supports manual version bumping (patch/minor/major)

## 🔧 Setup Instructions

### Step 1: Configure PyPI API Tokens

1. **Create PyPI Account**: Sign up at [pypi.org](https://pypi.org)
2. **Create Test PyPI Account**: Sign up at [test.pypi.org](https://test.pypi.org)
3. **Generate API Tokens**:
   - PyPI: Go to Account settings → API tokens → Add API token
   - Test PyPI: Go to Account settings → API tokens → Add API token

### Step 2: Add GitHub Secrets

In your GitHub repository, go to `Settings → Secrets and variables → Actions` and add:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `PYPI_API_TOKEN` | `pypi-...` | Your PyPI API token |
| `TEST_PYPI_API_TOKEN` | `pypi-...` | Your Test PyPI API token |

### Step 3: Configure Repository Settings

1. **Enable Actions**: Go to `Settings → Actions → General` and ensure actions are enabled
2. **Branch Protection**: Consider protecting your `main` branch
3. **Permissions**: Ensure the repository has write permissions for actions

## 🚀 Usage Instructions

### Automated Deployment via Tags

1. **Update version** in `pyproject.toml`:
   ```toml
   version = "0.1.4"
   ```

2. **Commit and push** changes:
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to 0.1.4"
   git push
   ```

3. **Create and push a tag**:
   ```bash
   git tag v0.1.4
   git push origin v0.1.4
   ```

4. **Automatic deployment** will trigger and deploy to PyPI!

### Manual Deployment

1. Go to **Actions** tab in your repository
2. Select **"Deploy to PyPI"** workflow
3. Click **"Run workflow"**
4. Choose the branch and run
5. This will deploy to **Test PyPI** for testing

### Creating Releases

#### Automatic Release Creation
- When you update the version in `pyproject.toml` and push to `main`, a GitHub release will be created automatically

#### Manual Release Creation
1. Go to **Actions** tab
2. Select **"Release"** workflow  
3. Click **"Run workflow"**
4. Choose version bump type: `patch`, `minor`, or `major`
5. A new release will be created with the bumped version

## 📝 Workflow Details

### Testing Matrix
- **Python Versions**: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12
- **Operating System**: Ubuntu Latest
- **Coverage**: Codecov integration for coverage reports

### Security Features
- **Dependency scanning** with `safety`
- **Code security scan** with `bandit`
- **Token-based authentication** for PyPI

### Quality Assurance
- **Code formatting** with `black`
- **Linting** with `flake8`
- **Testing** with `pytest`
- **Package validation** with `twine check`

## 🔄 Development Workflow

### For Contributors
1. **Fork** and clone the repository
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make changes** and add tests
4. **Run tests locally**: `pytest tests/`
5. **Format code**: `black .`
6. **Create Pull Request** - CI will run automatically

### For Maintainers
1. **Review and merge** Pull Requests
2. **Update version** in `pyproject.toml` when ready for release
3. **Create tag** for automatic PyPI deployment
4. **GitHub release** will be created automatically

## 🏷️ Version Tagging Convention

- **Patch**: `v0.1.4` (bug fixes)
- **Minor**: `v0.2.0` (new features, backward compatible)
- **Major**: `v1.0.0` (breaking changes)

## 🔍 Troubleshooting

### Common Issues

1. **PyPI Token Invalid**: 
   - Check if token is correctly set in GitHub secrets
   - Ensure token has proper permissions

2. **Tests Failing**:
   - Check the Actions tab for detailed error logs
   - Ensure all tests pass locally before pushing

3. **Version Conflicts**:
   - Make sure the version in `pyproject.toml` hasn't already been published
   - PyPI doesn't allow re-uploading the same version

4. **Permission Errors**:
   - Ensure repository has proper workflow permissions
   - Check if branch protection rules are blocking pushes

### Getting Help

- Check the **Actions** tab for detailed logs
- Review the **Issues** tab for known problems
- Refer to [GitHub Actions documentation](https://docs.github.com/en/actions)

## 📚 Additional Resources

- [PyPI Publishing Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Codecov Documentation](https://docs.codecov.io/)

---

**Happy coding!** 🎉
