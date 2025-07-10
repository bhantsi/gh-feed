# gh-feed

![PyPI](https://img.shields.io/pypi/v/gh-feed)
![License](https://img.shields.io/github/license/bhantsi/gh-feed)
![Issues](https://img.shields.io/github/issues/bhantsi/gh-feed)


**gh-feed** is a command-line tool written in Python that fetches and displays a GitHub user's recent public activity directly in the terminal.  
It uses the GitHub API and works with no external libraries.

## 🚀 Features

- **Fetches GitHub activity** - Get the most recent public events for any GitHub user
- **Rich event support** - Supports pushes, issues, pull requests, stars, forks, releases, comments, and more
- **Beautiful output** - Colorized terminal output with relative timestamps (e.g., "2h ago")
- **Smart filtering** - Filter events by type using `--filter <event_type>`
- **Export functionality** - Export results to JSON with `--json` flag
- **Authentication support** - Use GitHub tokens via `--token` or `GITHUB_TOKEN` env variable
- **Interactive mode** - Step-by-step guided usage with `--interactive`
- **Offline caching** - Caches API responses for 5 minutes to reduce API calls
- **Error handling** - Graceful handling of rate limits, network issues, and invalid users
- **Update notifications** - Automatic check for new versions with upgrade instructions
- **Version information** - Check current version with `--version` or `-v`
- **Comprehensive help** - Detailed usage guide with `--help` or `-h`
- **No dependencies** - Pure Python standard library, no external packages required

---

## 📦 Installation

### From PyPI (Recommended)

Install the latest stable version from PyPI:

```bash
pip install gh-feed
```

### From TestPyPI (Development)

For testing pre-release versions, you can install from TestPyPI:

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps gh-feed
```

### Development Installation

For development or contributing:

```bash
git clone https://github.com/bhantsi/gh-feed.git
cd gh-feed
pip install -e .
```

## 🔄 Automated Deployment

This project uses GitHub Actions for automated testing and deployment:

- **Continuous Integration**: Runs tests on all supported Python versions
- **Automated PyPI Deployment**: Deploys to PyPI when version tags are pushed
- **Security Scanning**: Automated security and dependency checks
- **Code Quality**: Automated linting and formatting checks

### For Contributors

1. Fork the repository
2. Create a feature branch
3. Make your changes and add tests
4. Create a Pull Request
5. CI will automatically run tests and checks

### For Maintainers

1. Update version in `pyproject.toml`
2. Create and push a version tag (e.g., `v0.1.4`)
3. GitHub Actions will automatically deploy to PyPI

> **Note:**  
> The package is automatically published to PyPI when new version tags are created. Manual releases can also be triggered through GitHub Actions.

---

## 🛠️ Usage

### Prerequisites
- Python 3 (comes pre-installed on most systems)

### Running the CLI

After installation, you can run the CLI from anywhere:

```bash
gh-feed <github_username>
```

Or, if you want to run the script directly (if you have the source):

```bash
python3 app.py <github_username>
```

### Basic Commands

```bash
# Get user activity
gh-feed octocat

# Show version
gh-feed --version
gh-feed -v

# Show help
gh-feed --help
gh-feed -h

# Interactive mode
gh-feed --interactive
```

### Filtering Events

You can filter by event type (e.g., only show push events):

```bash
gh-feed octocat --filter PushEvent
```

### Exporting to JSON

Export the latest events to a file:

```bash
gh-feed octocat --json
```

You can combine filtering and export:

```bash
gh-feed octocat --filter IssuesEvent --json
```

### Using a GitHub Token

To increase your API rate limit, you can provide a personal access token:

```bash
gh-feed octocat --token <your_github_token>
```

Or set the `GITHUB_TOKEN` environment variable:

```bash
export GITHUB_TOKEN=your_github_token
gh-feed octocat
```

### Interactive Mode

Start an interactive session for guided usage:

```bash
gh-feed --interactive
```
You'll be prompted for the username, event filter, token, and export options.

### Caching

API responses are cached for 5 minutes in the `~/.cache/gh-feed/` directory to reduce API calls and speed up repeated queries.

### Update Notifications

The tool automatically checks for new versions when you run commands and notifies you if an update is available:

```
📦 New version available: 0.1.4 (current: 0.1.3)
💡 Run 'pip install --upgrade gh-feed' to update
```

### Example

```bash
gh-feed octocat
```

Sample output:
```
- Pushed 2 commits to octocat/Hello-World (3h ago)
- Opened an issue in octocat/Hello-World (5h ago)
- Starred octocat/Spoon-Knife (1d ago)

Summary:
- push commit: 1
- issue opened: 1
- repo starred: 1
- Activity in 3 repos
```

---

## ⚠️ Important Notes

- The tool uses the public GitHub API, which is subject to [rate limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting). If you make too many requests in a short period, you may be temporarily blocked from making further requests.
- Only public events are shown. Private activity will not appear.
- If you see a warning about nearing the rate limit, wait a while before making more requests.
- Make sure you have an active internet connection.
- The tool displays up to 7 of the most recent events.
- Cached data is stored in `~/.cache/gh-feed/` and is valid for 5 minutes.

---

## � Changelog

### v0.1.3 (Latest)
- ✅ **NEW**: Added `--help` and `-h` command support for comprehensive usage guide
- ✅ **NEW**: Added `--version` and `-v` command to display current version
- ✅ **NEW**: Automatic update notifications when newer versions are available
- 🐛 **FIXED**: Interactive mode now properly validates empty username input
- 🐛 **FIXED**: Help command now works correctly with installed package
- 📚 **IMPROVED**: Enhanced help documentation with examples and options
- 🎨 **IMPROVED**: Better error handling and user experience

### v0.1.2
- 🚀 **NEW**: Offline caching system for API responses (5-minute cache)
- 🚀 **NEW**: Interactive mode with guided prompts
- 🚀 **NEW**: Colorized terminal output for better readability
- 🚀 **NEW**: Event filtering by type with `--filter` option
- 🚀 **NEW**: JSON export functionality with `--json` flag
- 🚀 **NEW**: GitHub token authentication support
- 📚 **IMPROVED**: Comprehensive error handling for rate limits and network issues

### v0.1.1
- 🚀 **INITIAL**: Basic GitHub user activity fetching
- 🚀 **INITIAL**: Support for multiple event types
- 🚀 **INITIAL**: Relative timestamp display
- 🚀 **INITIAL**: Activity summary with repository count

### v0.1.0
- 🎉 Initial release
- ✅ Basic GitHub user activity fetching
- ✅ Support for multiple event types
- ✅ Relative timestamp display
- ✅ Activity summary with repository count

---

## �📝 Attribution

This project was inspired by the [GitHub User Activity CLI](https://roadmap.sh/projects/github-user-activity) project on [roadmap.sh](https://roadmap.sh/).  
Check out their project for more ideas and inspiration!

---

## 📈 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License
MIT License
