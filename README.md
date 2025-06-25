# gh-feed

**gh-feed** is a simple command-line tool written in Python that fetches and displays a GitHub user's recent public activity directly in the terminal.  
It uses the GitHub API and works with no external libraries.

---

## 🚀 Features

- Fetches the most recent public events for any GitHub user.
- Supports a variety of event types (push, issues, pull requests, stars, forks, etc.).
- Gracefully handles errors like invalid usernames, rate limits, and connection issues.
- Warns you when you're nearing GitHub's rate limit.

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

### Example

```bash
python3 app.py octocat
```

Sample output:
```
- Pushed 2 commits to octocat/Hello-World
- Opened an issue in octocat/Hello-World
- Starred octocat/Spoon-Knife
```

---

## ⚠️ Important Notes

- The tool uses the public GitHub API, which is subject to [rate limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting). If you make too many requests in a short period, you may be temporarily blocked from making further requests.
- Only public events are shown. Private activity will not appear.
- If you see a warning about nearing the rate limit, wait a while before making more requests.
- Make sure you have an active internet connection.

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
