# What is this

A dnsmasq being populated by DHCP reservations made in a UniFi controller.

# How does it work

It polls a UniFi controller (using an API client from here: https://github.com/frehov/Unifi-Python-API) and writes
client names and reserved IP addresses to a file being picked up by dnsmasq.

# How to set it up:

* Copy docker-compose.example.yml from here
* Set the relevant values for these environment variables:

| Name                    | Description                                   | Default value        |
|-------------------------|-----------------------------------------------|----------------------|
| `UNIFI_POLL_INTERVAL`   | Seconds between API calls to UniFi Controller | `60`                 |
| `UNIFI_BASEURL`         | URL to UniFi controller                       | `https://unifi:8443` |
| `UNIFI_USERNAME`        | Username to UniFi controller                  | -                    |
| `UNIFI_PASSWORD`        | Password to UniFi controller                  | -                    |

* `docker-compose up`
* UniFi clients with aliases and "fixed IP" (DHCP reservations) will be written to `/etc/dnsmasq.d/unifi.hosts`.
* dnsmasq will look in `/etc/dnsmasq.d` and read `*.conf` files as additional config files and `*.hosts` files as additional host files, so feel free to put any additional stuff there.
