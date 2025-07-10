# Makefile for gh-feed development

.PHONY: help install test lint format clean build deploy-test deploy version-patch version-minor version-major

# Default target
help:
	@echo "Available commands:"
	@echo "  install        Install development dependencies"
	@echo "  test           Run tests"
	@echo "  lint           Run linting checks"
	@echo "  format         Format code with black"
	@echo "  clean          Clean build artifacts"
	@echo "  build          Build package"
	@echo "  deploy-test    Deploy to Test PyPI"
	@echo "  deploy         Deploy to PyPI (use with caution)"
	@echo "  version-patch  Bump patch version"
	@echo "  version-minor  Bump minor version"
	@echo "  version-major  Bump major version"

# Install development dependencies
install:
	pip install -e .
	pip install pytest pytest-cov black flake8 build twine

# Run tests
test:
	pytest tests/ -v --cov=gh_feed --cov-report=term-missing

# Run linting
lint:
	flake8 gh_feed/ tests/
	black --check gh_feed/ tests/

# Format code
format:
	black gh_feed/ tests/

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Build package
build: clean
	python -m build

# Deploy to Test PyPI
deploy-test: build
	twine upload --repository testpypi dist/*

# Deploy to PyPI (use with caution)
deploy: build
	twine upload dist/*

# Version bumping using the script
version-patch:
	python scripts/bump_version.py patch

version-minor:
	python scripts/bump_version.py minor

version-major:
	python scripts/bump_version.py major

# Development server for testing
dev:
	python -m gh_feed.app --help
