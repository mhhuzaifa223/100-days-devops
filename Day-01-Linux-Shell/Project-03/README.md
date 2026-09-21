# Project 03 — Automated User Management System

## Objective

Automate common Linux user and group management tasks using Bash.

The script creates a user, creates a group, adds the user to the group, creates an application directory, and configures ownership and permissions.

## Technologies

* Linux
* Bash
* `useradd`
* `groupadd`
* `usermod`
* `id`
* `getent`
* `groups`
* `grep`
* `chown`
* `chmod`

## How It Works

```text
Check User
    ↓
Create User if Needed
    ↓
Check Group
    ↓
Create Group if Needed
    ↓
Add User to Group
    ↓
Create /app Directory
    ↓
Set Ownership
    ↓
Set Permissions
```

The application directory is configured with:

```text
Owner: root
Group: developers
Permissions: 770
```

This allows the owner and members of the `developers` group to access the directory while preventing access from other users.

## How to Run

```bash
chmod +x user_management.sh
./user_management.sh
```

The script uses `sudo` for operations that require administrative privileges.

## Example Output

```text
User Jack already exist
Group developers already exists
Jack is already in developers
Directory /app already exists
Ownership set to root:developers
Permission set to 770
```

## Testing

The directory permissions were verified with:

```bash
ls -ld /app
```

Expected configuration:

```text
drwxrwx--- root developers /app
```

User group membership was checked with:

```bash
groups seed
```

## Troubleshooting

A permission issue was intentionally tested by accessing `/app` with a user who was not a member of the `developers` group.

The issue was investigated by checking:

```bash
groups username
ls -ld /app
```

The user was then added to the required group:

```bash
sudo usermod -aG developers username
```

A new shell session was required for the updated group membership to take effect.

## Key Concepts Learned

* Linux users and groups
* Supplementary groups
* Least-privilege access
* Directory ownership
* File and directory permissions
* `chmod 770`
* `chown`
* User existence checks
* Group existence checks
* Idempotent automation
* Permission troubleshooting
