#!/bin/sh
unifi_hosts=/etc/dnsmasq.d/unifi.hosts

dnsmasq -k --addn-hosts=/etc/dnsmasq.d --log-facility=- ${DNSMASQ_OPTS} &
dnsmasq_pid=$!

touch /etc/dnsmasq.d/unifi.hosts
while true; do
    hosts_before=$(cat $unifi_hosts)
    ./get_unifi_reservations.py > $unifi_hosts
    hosts_after=$(cat $unifi_hosts)
    if [ "$hosts_before" != "$hosts_after" ]; then
        kill -HUP $dnsmasq_pid
    fi
    sleep ${UNIFI_POLL_INTERVAL:-60}
done

