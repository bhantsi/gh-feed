#!/usr/bin/env python3

import sys
import os
import urllib.request
import urllib.error
import json
from datetime import datetime, timezone
from collections import Counter
import time

API_URL = "https://api.github.com/users/{}/events"

# ANSI color codes
COLORS = {
    "PushEvent": "\033[92m",      # Green
    "IssuesEvent": "\033[94m",    # Blue
    "WatchEvent": "\033[93m",     # Yellow
    "CreateEvent": "\033[96m",    # Cyan
    "ForkEvent": "\033[95m",      # Magenta
    "PullRequestEvent": "\033[91m",  # Red
    "PullRequestReviewCommentEvent": "\033[90m",  # Dark Gray
    "DeleteEvent": "\033[31m",    # Bright Red
    "ReleaseEvent": "\033[35m",   # Purple
    "default": "\033[0m"           # Reset/No color
}

RESET = "\033[0m"

CACHE_DIR = ".gh_feed_cache"
CACHE_EXPIRY = 300  # seconds (5 minutes)


def get_cache_path(username):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    return os.path.join(CACHE_DIR, f"{username}.json")


def load_cache(username):
    path = get_cache_path(username)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r") as f:
            cached = json.load(f)
        # Check expiry
        if time.time() - cached.get("timestamp", 0) < CACHE_EXPIRY:
            return cached.get("events")
    except Exception:
        pass
    return None


def save_cache(username, events):
    path = get_cache_path(username)
    try:
        with open(path, "w") as f:
            json.dump({"timestamp": time.time(), "events": events}, f)
    except Exception:
        pass


def fetch_user_activity(username, token=None, use_cache=True):
    # Try cache first
    if use_cache:
        cached_events = load_cache(username)
        if cached_events is not None:
            print(f"(Loaded cached activity for '{username}')")
            return cached_events

    url = API_URL.format(username)
    try:
        request = urllib.request.Request(url)
        if token:
            request.add_header("Authorization", f"token {token}")

        with urllib.request.urlopen(request) as response:
            headers = response.getheaders()
            rate_limit_remaining = dict(headers).get("X-RateLimit-Remaining")
            if rate_limit_remaining is not None and int(rate_limit_remaining) <= 5:
                print(
                    f"Warning: You are nearing the GitHub API rate limit. Only {rate_limit_remaining} requests remaining.")
            data = response.read()
            events = json.loads(data)
            save_cache(username, events)
            return events
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        elif e.code == 403:
            print("Error: Rate limit exceeded. Try again later.")
        else:
            print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
        # Try to load cache even if offline
        cached_events = load_cache(username)
        if cached_events is not None:
            print(f"(Loaded cached activity for '{username}' - offline mode)")
            return cached_events
    return None


def time_ago(iso_time):
    event_time = datetime.strptime(
        iso_time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    delta = now - event_time

    seconds = delta.total_seconds()
    if seconds < 60:
        return f"{int(seconds)}s ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)}h ago"
    else:
        return f"{int(seconds // 86400)}d ago"


def colorize(text, event_type):
    color = COLORS.get(event_type, COLORS["default"])
    return f"{color}{text}{RESET}"


def display_activity(events, filter_type=None):
    if not events:
        print("No recent public activity found.")
        return

    count = 0
    type_counter = Counter()
    repos = set()

    for event in events:
        if count >= 7:
            break

        type = event["type"]
        if filter_type and filter_type.lower() not in type.lower():
            continue

        type_counter[type] += 1
        repos.add(event["repo"]["name"])

        repo = event["repo"]["name"]
        created_at = event.get("created_at", "")
        timestamp = f"({time_ago(created_at)})" if created_at else ""

        if type == "PushEvent":
            commit_count = len(event["payload"]["commits"])
            message = f"- Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {repo} {timestamp}"
        elif type == "IssuesEvent":
            action = event["payload"]["action"]
            message = f"- {action.capitalize()} an issue in {repo} {timestamp}"
        elif type == "WatchEvent":
            message = f"- Starred {repo} {timestamp}"
        elif type == "CreateEvent":
            ref_type = event["payload"]["ref_type"]
            message = f"- Created a new {ref_type} in {repo} {timestamp}"
        elif type == "ForkEvent":
            forkee = event["payload"]["forkee"]["full_name"]
            message = f"- Forked {repo} to {forkee} {timestamp}"
        elif type == "PullRequestEvent":
            action = event["payload"]["action"]
            message = f"- {action.capitalize()} a pull request in {repo} {timestamp}"
        elif type == "PullRequestReviewCommentEvent":
            message = f"- Commented on a pull request in {repo} {timestamp}"
        elif type == "DeleteEvent":
            ref_type = event["payload"]["ref_type"]
            ref = event["payload"]["ref"]
            message = f"- Deleted {ref_type} '{ref}' in {repo} {timestamp}"
        elif type == "ReleaseEvent":
            action = event["payload"]["action"]
            release_name = event["payload"]["release"]["name"]
            message = f"- {action.capitalize()} release '{release_name}' in {repo} {timestamp}"
        else:
            message = f"- {type} in {repo} {timestamp}"

        print(colorize(message, type))
        count += 1

    if count > 0:
        print("\nSummary:")
        for etype, num in type_counter.items():
            if etype == "PushEvent":
                label = "push commit"
            elif etype == "IssuesEvent":
                label = "issue opened"
            elif etype == "PullRequestEvent":
                label = "pull request sent"
            elif etype == "WatchEvent":
                label = "repo starred"
            elif etype == "ForkEvent":
                label = "repo forked"
            elif etype == "CreateEvent":
                label = "repo created"
            elif etype == "DeleteEvent":
                label = "item deleted"
            elif etype == "ReleaseEvent":
                label = "release published"
            elif etype == "PullRequestReviewCommentEvent":
                label = "PR comment"
            else:
                label = etype

            print(f"- {label}: {num}")

        print(f"- Activity in {len(repos)} repos")


def export_to_json(events, filename="activity.json"):
    try:
        with open(filename, "w") as f:
            json.dump(events[:7], f, indent=2)
        print(f"Exported events to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")


def interactive_mode():
    print("Welcome to Interactive Mode!")
    username = input("Enter GitHub username: ").strip()
    token = os.getenv("GITHUB_TOKEN")

    token_choice = input("Use GitHub token? (y/n): ").strip().lower()
    if token_choice == 'y':
        token_input = input(
            "Enter GitHub token (leave blank to use $GITHUB_TOKEN): ").strip()
        if token_input:
            token = token_input

    filter_type = input("Filter by event type (leave blank for all): ").strip()
    export = input("Export results to JSON? (y/n): ").strip().lower() == 'y'

    events = fetch_user_activity(username, token)
    if events is not None:
        display_activity(events, filter_type if filter_type else None)
        if export:
            export_to_json(events)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--interactive":
        interactive_mode()
        return

    if len(sys.argv) < 2:
        print(
            "Usage: gh-feed <github_username> [--filter <event_type>] [--json] [--token <token>] | --interactive")
        sys.exit(1)

    username = sys.argv[1]
    filter_type = None
    export_json = "--json" in sys.argv
    token = os.getenv("GITHUB_TOKEN")

    if "--token" in sys.argv:
        try:
            token_index = sys.argv.index("--token")
            token = sys.argv[token_index + 1]
        except IndexError:
            print("Error: --token flag must be followed by a token")
            sys.exit(1)

    if "--filter" in sys.argv:
        try:
            filter_index = sys.argv.index("--filter")
            filter_type = sys.argv[filter_index + 1]
        except IndexError:
            print("Error: --filter flag must be followed by an event type")
            sys.exit(1)

    events = fetch_user_activity(username, token)

    if events is not None:
        display_activity(events, filter_type)
        if export_json:
            export_to_json(events)


if __name__ == "__main__":
    main()
