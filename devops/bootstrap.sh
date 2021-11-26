#!/bin/bash

# execute using:
# ssh root@$IP < bootstrap.sh

export PATH=$PATH:/usr/bin
export NEW_USER=ubuntu

# Ubuntu update and few tools
sudo apt-get update
sudo apt-get install -y vim htop build-essential \
     libssl-dev libffi-dev net-tools \
     python3-pip python-setuptools

# Creates a new user (as sudor)
adduser --disabled-password --gecos "" $NEW_USER
usermod -aG sudo $NEW_USER

# Copy the SSH Key to it (you can ssh using it instead of root)
mkdir /home/$NEW_USER/.ssh
chmod 700 /home/$NEW_USER/.ssh
sudo cp /root/.ssh/authorized_keys /home/$NEW_USER/.ssh/authorized_keys
sudo chown -R $NEW_USER:$NEW_USER /home/$NEW_USER/.ssh
sudo chmod 600 /home/$NEW_USER/.ssh/authorized_keys

echo ' ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

