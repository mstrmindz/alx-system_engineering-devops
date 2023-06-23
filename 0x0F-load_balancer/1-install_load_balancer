#!/bin/bash

# Update package lists and upgrade installed packages
sudo apt update
sudo apt upgrade -y

# Install HAproxy
sudo apt install -y haproxy

# Configure HAproxy to send traffic to web-01 and web-02
sudo bash -c 'cat << EOF > /etc/haproxy/haproxy.cfg
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000
    timeout client 50000
    timeout server 50000

frontend http_front
    bind *:80
    stats uri /haproxy?stats
    default_backend http_back

backend http_back
    balance roundrobin
    server web-01 135158-web-01:80 check
    server web-02 135158-web-02:80 check
EOF'

# Restart HAproxy service
sudo service haproxy restart

# Add current user to 'haproxy' group
sudo usermod -aG haproxy $USER

# Print completion message
echo "Machine configuration completed."
