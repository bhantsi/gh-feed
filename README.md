# gh-feed

**gh-feed** is a simple command-line tool written in Python that fetches and displays a GitHub user's recent public activity directly in the terminal.  
It uses the GitHub API and works with no external libraries.

---

## 🚀 Features

- Fetches the most recent public events for any GitHub user.
- Supports a variety of event types: push, issues, pull requests, stars, forks, releases, comments, and more.
- Colorizes output for better readability in the terminal.
- Summarizes activity by event type and repository count.
- Allows filtering events by type using the `--filter <event_type>` flag.
- Exports the latest events to a JSON file with the `--json` flag.
- Gracefully handles errors like invalid usernames, rate limits, and connection issues.
- Warns you when you're nearing GitHub's rate limit.
- Shows relative timestamps (e.g., "2h ago") for each event.
- Requires no external dependencies—pure Python standard library.

---

## 🛠️ Usage

### Prerequisites
- Python 3 (comes pre-installed on most systems)

### Running the CLI

```bash
chmod +x app.py
./app.py <github_username>
```

Or run directly with Python:

```bash
python3 app.py <github_username>
```

### Filtering Events

You can filter by event type (e.g., only show push events):

```bash
python3 app.py octocat --filter PushEvent
```

### Exporting to JSON

Export the latest events to a file:

```bash
python3 app.py octocat --json
```

You can combine filtering and export:

```bash
python3 app.py octocat --filter IssuesEvent --json
```

### Example

```bash
python3 app.py octocat
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

---

## 📝 Attribution

This project was inspired by the [GitHub User Activity CLI](https://roadmap.sh/projects/github-user-activity) project on [roadmap.sh](https://roadmap.sh/).  
Check out their project for more ideas and inspiration!

---

## 📈 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License
MIT License
