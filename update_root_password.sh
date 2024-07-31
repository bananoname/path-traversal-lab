#!/bin/bash

# Generate a random password
NEW_PASSWORD=$(openssl rand -base64 12)

# Update the root password
echo "root:$NEW_PASSWORD" | chpasswd

# Print the new password to the logs
echo "The new root password is: $NEW_PASSWORD"

# Execute the original command
exec "$@"
