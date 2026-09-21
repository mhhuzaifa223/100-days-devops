#!/bin/bash

echo "========= Linux Server Hardening =========="

if sudo ufw status | grep -q "22"; then
   echo "SSH port 22 is already allowed"

else
   sudo ufw allow 22
   echo "SSH port 22 allowed"
fi

if sudo ufw status | grep -q "Status: active"; then
   echo "UFW is already active"
else 
   sudo ufw enable
   echo "UFW enabled"
fi

echo "Checking SSH password authentication..."

if ! sudo sshd -T | grep -qi "passwordauthentication no"; then
    sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
    echo "SSH password authentication disabled"
else
    echo "SSH password authentication already disabled"
fi

echo "Checking SSH root login..."

if ! sudo sshd -T | grep -qi "permitrootlogin no"; then
    sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
    echo "Direct root SSH login disabled"
else
    echo "Direct root SSH login already disabled"
fi

echo "Validating SSH configuration..."

if sudo sshd -t; then
    echo "SSH configuration is valid"
else
    echo "ERROR: SSH configuration is invalid"
    exit 1
fi

echo "Reloading SSH service..."

sudo systemctl reload ssh

if systemctl is-active --quiet ssh; then
    echo "SSH service is running"
else
    echo "ERROR: SSH service is not running"
    exit 1
fi
