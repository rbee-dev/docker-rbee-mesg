#! /bin/bash

NAMESERVER=`cat /etc/resolv.conf | grep -m 1 nameserver | awk '{ print $2 }'`:53
sed -ri 's/(dns1).*/\1 '$NAMESERVER'/' /etc/haproxy.cfg

exec haproxy -V -f /haproxy.cfg
