#!/usr/bin/env python3
"""
Version bump utility for gh-feed package.
Usage: python scripts/bump_version.py [patch|minor|major]
"""

import re
import sys
import subprocess
from pathlib import Path


def get_current_version():
    """Read current version from pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")

    content = pyproject_path.read_text()
    match = re.search(r'^version = "([^"]+)"', content, re.MULTILINE)
    if not match:
        raise ValueError("Version not found in pyproject.toml")

    return match.group(1)


def bump_version(current_version, bump_type):
    """Bump version based on type"""
    major, minor, patch = map(int, current_version.split("."))

    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    elif bump_type == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError("bump_type must be 'major', 'minor', or 'patch'")


def update_version_in_file(new_version):
    """Update version in pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()

    # Update version
    new_content = re.sub(
        r'^version = "([^"]+)"',
        f'version = "{new_version}"',
        content,
        flags=re.MULTILINE,
    )

    pyproject_path.write_text(new_content)


def run_git_commands(new_version):
    """Run git commands to commit and tag"""
    try:
        # Add changes
        subprocess.run(["git", "add", "pyproject.toml"], check=True)

        # Commit changes
        subprocess.run(
            ["git", "commit", "-m", f"Bump version to {new_version}"], check=True
        )

        # Create tag
        subprocess.run(["git", "tag", f"v{new_version}"], check=True)

        print(f"✅ Version bumped to {new_version}")
        print(f"✅ Committed changes and created tag v{new_version}")
        print("\n📝 Next steps:")
        print("1. Push changes: git push")
        print(f"2. Push tag: git push origin v{new_version}")
        print("3. This will trigger automatic deployment to PyPI!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git command failed: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/bump_version.py [patch|minor|major]")
        sys.exit(1)

    bump_type = sys.argv[1].lower()
    if bump_type not in ["patch", "minor", "major"]:
        print("❌ Bump type must be 'patch', 'minor', or 'major'")
        sys.exit(1)

    try:
        # Get current version
        current_version = get_current_version()
        print(f"📋 Current version: {current_version}")

        # Calculate new version
        new_version = bump_version(current_version, bump_type)
        print(f"🚀 New version: {new_version}")

        # Confirm with user
        response = input(f"Are you sure you want to bump to {new_version}? (y/N): ")
        if response.lower() != "y":
            print("❌ Operation cancelled")
            sys.exit(0)

        # Update version in file
        update_version_in_file(new_version)
        print(f"✅ Updated pyproject.toml with version {new_version}")

        # Run git commands
        run_git_commands(new_version)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
