#!/usr/bin/env python3

import sys
import urllib.request
import urllib.error
import json

API_URL = "https://api.github.com/users/{}/events"


def fetch_user_activity(username):
    url = API_URL.format(username)
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = response.getheaders()
            rate_limit_remaining = dict(headers).get("X-RateLimit-Remaining")
            if rate_limit_remaining is not None and int(rate_limit_remaining) <= 5:
                print(
                    f"Warning: You are nearing the GitHub API rate limit. Only {rate_limit_remaining} requests remaining.")
            data = response.read()
            return json.loads(data)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        elif e.code == 403:
            print("Error: Rate limit exceeded. Try again later.")
        else:
            print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
    return None


def display_activity(events):
    if not events:
        print("No recent public activity found.")
        return

    for event in events:
        type = event["type"]
        repo = event["repo"]["name"]

        if type == "PushEvent":
            count = len(event["payload"]["commits"])
            print(
                f"- Pushed {count} commit{'s' if count > 1 else ''} to {repo}")
        elif type == "IssuesEvent":
            action = event["payload"]["action"]
            print(f"- {action.capitalize()} an issue in {repo}")
        elif type == "WatchEvent":
            print(f"- Starred {repo}")
        elif type == "CreateEvent":
            ref_type = event["payload"]["ref_type"]
            print(f"- Created a new {ref_type} in {repo}")
        elif type == "ForkEvent":
            forkee = event["payload"]["forkee"]["full_name"]
            print(f"- Forked {repo} to {forkee}")
        elif type == "PullRequestEvent":
            action = event["payload"]["action"]
            print(f"- {action.capitalize()} a pull request in {repo}")
        elif type == "PullRequestReviewCommentEvent":
            print(f"- Commented on a pull request in {repo}")
        elif type == "DeleteEvent":
            ref_type = event["payload"]["ref_type"]
            ref = event["payload"]["ref"]
            print(f"- Deleted {ref_type} '{ref}' in {repo}")
        elif type == "ReleaseEvent":
            action = event["payload"]["action"]
            release_name = event["payload"]["release"]["name"]
            print(f"- {action.capitalize()} release '{release_name}' in {repo}")
        else:
            print(f"- {type} in {repo}")  # fallback for unhandled events


def main():
    if len(sys.argv) != 2:
        print("Usage: gh-feed <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_user_activity(username)

    if events is not None:
        display_activity(events)


if __name__ == "__main__":
    main()
