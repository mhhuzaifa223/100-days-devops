#!/bin/bash

USERNAME="Jack"

if id "$USERNAME" &>/dev/null; then
   echo "User $USERNAME already exist"
else
   sudo useradd -m "$USERNAME"
   echo "User $USERNAME Created Successfully"
fi
GROUP="developers"

if getent group "$GROUP" > /dev/null; then
   echo "Group $GROUP already exists"
else
   sudo groupadd "$GROUP"
   echo "Group $GROUP Created Successfully"
fi

if groups "$USERNAME" | grep -qw "$GROUP"; then
   echo "$USERNAME is already in $GROUP"
else
   sudo usermod -aG "$GROUP" "$USERNAME"
   echo "Added $USERNAME to $GROUP"
fi

APP_DIR="/app"

if [ -d "$APP_DIR" ]; then
   echo "Directory $APP_DIR already exists"
else 
   sudo mkdir "$APP_DIR"
   echo "Directory $APP_DIR created successfully"
fi

sudo chown root:"$GROUP" "$APP_DIR"
echo "Ownership set to root:$GROUP"

sudo chmod 770 "$APP_DIR"
echo "Permission set to 770"
