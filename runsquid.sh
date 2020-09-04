#!/bin/sh

echo "-=[ Building any sibling proxy hand-offs from mounted /peerproxy.yml ]=-"
[ -f /peerproxy.yml ] && \
    /peerproxy.py \
        /peerproxy.yml \
        /peerproxy.conf.j2 \
        /etc/squid/squid.d/099-peerproxy.conf
echo "-=[ Checking cache directories. ]=-"
/usr/sbin/squid -Nz 2>&1
echo "-=[ Running for real. ]=-"
/usr/sbin/squid -N 2>&1
