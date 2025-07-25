# Development Guide for gh-feed

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+ 
- pip (Python package installer)
- Git

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bhantsi/gh-feed.git
   cd gh-feed
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**:
   ```bash
   pip install -e .
   ```

4. **Install development dependencies**:
   ```bash
   pip install pytest pytest-cov build twine
   ```

## 🧪 Testing

### Run Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=gh_feed --cov-report=html

# Run specific test
python -m pytest tests/test_app.py::test_specific_function -v
```

### Test Coverage
```bash
# Generate coverage report
python -m pytest tests/ --cov=gh_feed --cov-report=html
# Open htmlcov/index.html in browser to view coverage
```

## 🏗️ Building and Packaging

### Build the Package
```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build
```

### Test the Built Package
```bash
# Install from local build
pip install dist/gh_feed-*.whl

# Test installation
gh-feed --version
```

## 📦 Manual Deployment to PyPI

### Prerequisites
- PyPI account: https://pypi.org/account/register/
- TestPyPI account: https://test.pypi.org/account/register/
- API tokens for both PyPI and TestPyPI

### Step 1: Update Version
Edit `pyproject.toml` and update the version:
```toml
[project]
name = "gh-feed"
version = "0.1.5"  # Update this
```

### Step 2: Build the Package
```bash
# Clean and build
rm -rf build/ dist/ *.egg-info/
python -m build
```

### Step 3: Test on TestPyPI (Optional)
```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --no-deps gh-feed
```

### Step 4: Deploy to PyPI
```bash
# Upload to PyPI
python -m twine upload dist/*

# Verify deployment
pip install gh-feed
```

## 🔧 Development Commands

### Useful Commands
```bash
# Format code (if using black)
python -m black gh_feed/ tests/

# Lint code (if using flake8)
python -m flake8 gh_feed/ tests/

# Run the tool locally
python -m gh_feed <username>

# Or directly
python gh_feed/app.py <username>
```

## 📋 Code Style Guidelines

- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Add type hints where appropriate

## 🐛 Debugging

### Common Issues
1. **Import errors**: Make sure you installed in development mode (`pip install -e .`)
2. **API rate limits**: Use a GitHub token for higher limits
3. **Cache issues**: Clear cache directory `~/.cache/gh-feed/`

### Debug Mode
```bash
# Add debug output to your code
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📝 Adding New Features

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/new-feature-name
   ```

2. **Make your changes**:
   - Add new functionality
   - Write tests for new features
   - Update documentation

3. **Test your changes**:
   ```bash
   python -m pytest tests/ -v
   python -m gh_feed test-username  # Manual testing
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Add new feature: description"
   git push origin feature/new-feature-name
   ```

5. **Create a Pull Request** on GitHub

## 🚀 Release Process

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG** (if you have one)
3. **Run tests** to ensure everything works
4. **Build and test** the package locally
5. **Deploy to TestPyPI** for testing
6. **Deploy to PyPI** for release
7. **Create a git tag** for the release:
   ```bash
   git tag v0.1.5
   git push origin v0.1.5
   ```

## 🤝 Contributing Guidelines

- Fork the repository
- Create feature branches
- Write tests for new functionality
- Ensure all tests pass
- Follow the code style guidelines
- Submit pull requests with clear descriptions

## 📚 Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Documentation](https://pypi.org/help/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
