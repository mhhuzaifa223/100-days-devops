# Project 04 — Linux Server Hardening Automation

## Objective

Automate basic Linux server hardening tasks using Bash.

The script configures firewall access, hardens SSH authentication, disables direct root login, validates the SSH configuration, and verifies that the SSH service remains operational.

## Technologies

* Linux
* Bash
* UFW
* OpenSSH
* `sshd`
* `systemctl`
* `sed`
* `grep`

## How It Works

```text
Check UFW
    ↓
Allow SSH Port 22
    ↓
Enable Firewall
    ↓
Disable SSH Password Authentication
    ↓
Disable Direct Root Login
    ↓
Validate SSH Configuration
    ↓
Reload SSH
    ↓
Verify SSH Service
```

The script is designed to be **idempotent**, meaning running it multiple times does not repeatedly make unnecessary changes.

## Security Configuration

The final SSH configuration includes:

```text
Password authentication → Disabled
Direct root login       → Disabled
SSH key authentication  → Enabled
SSH port                → 22
UFW                     → Enabled
```

UFW uses:

```text
Incoming → Deny by default
Outgoing → Allow by default
```

## How to Run

```bash
chmod +x hardening.sh
./hardening.sh
```

Administrative operations use `sudo`.

## Example Output

```text
========= Linux Server Hardening ==========
SSH port 22 is already allowed
UFW is already active
SSH password authentication already disabled
Direct root SSH login already disabled
SSH configuration is valid
SSH service is running
```

## Testing

The script was tested for idempotency by running it multiple times.

The first execution applied the required configuration.

Subsequent executions detected that the configuration was already correct and avoided unnecessary changes.

## Failure Testing

An invalid SSH configuration directive was intentionally added to `/etc/ssh/sshd_config`.

The configuration was detected as invalid using:

```bash
sudo sshd -t
```

The invalid configuration was removed and the SSH configuration was validated again before reloading the service.

This demonstrated why configuration validation should happen before reloading SSH.

## Troubleshooting

When troubleshooting SSH hardening:

```bash
sudo sshd -t
```

checks the configuration syntax.

```bash
sudo sshd -T
```

shows the effective SSH configuration.

```bash
systemctl is-active ssh
```

checks whether the SSH service is running.

These checks help prevent configuration errors from causing SSH access problems.

## Key Concepts Learned

* Linux server hardening
* UFW firewall
* SSH security
* SSH key authentication
* Password authentication
* Root login restrictions
* Least privilege
* Configuration validation
* `sshd -t`
* `sshd -T`
* `systemctl`
* Idempotent automation
* Safe configuration changes
* Failure testing and recovery
