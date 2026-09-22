# Project 19 — Git Ignore & Secret Protection

## Goal

Learn how to prevent sensitive files such as `.env` from being accidentally committed to Git.

## What I Practiced

- Created a fake `.env` file containing a dummy AWS access key.
- Added `.env` to the root `.gitignore`.
- Verified Git was ignoring the file with `git check-ignore -v .env`.
- Confirmed `.env` remained ignored when using `git add .`.
- Learned that `.gitignore` does not remove secrets that were already committed.
- Learned why secret rotation is necessary if real credentials are exposed.
- Discovered and fixed an accidentally nested Git repository inside Project-11.

## Important Lesson

Never commit real AWS credentials, API keys, passwords, private keys, or other secrets.

Use `.gitignore` to prevent sensitive local files from being tracked.

If a real secret is accidentally committed, removing the file is not enough. The credential should be revoked or rotated immediately.
