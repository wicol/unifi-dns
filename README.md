# What it is

A dnsmasq being populated by DHCP reservations made in a UniFi controller.

# But why?

To make up for the fact that UniFi USG doesn't have hostname override for DHCP-reservations.

# How it works

It polls a UniFi controller and writes client names and reserved IP addresses to a file being picked up by dnsmasq.

# Configuration

## unifi-dns

* Copy `docker-compose.example.yml` from here
* Set the relevant values for these environment variables:

| Name                    | Description                                   | Default value        |
|-------------------------|-----------------------------------------------|----------------------|
| `UNIFI_BASEURL`         | URL to UniFi controller                       | `https://unifi:8443` |
| `UNIFI_USERNAME`        | Username to UniFi controller                  | -                    |
| `UNIFI_PASSWORD`        | Password to UniFi controller                  | -                    |
| `UNIFI_POLL_INTERVAL`   | Seconds between API calls to UniFi Controller | `60`                 |
| `UNIFI_SITE`            | UniFi "site" name                             | `default`            |

* `docker-compose up`
* UniFi clients with aliases and "fixed IP" (DHCP reservations) will be written to `/etc/dnsmasq.d/unifi.hosts`.
* dnsmasq will look in `/etc/dnsmasq.d` and read `*.conf` files as additional config files and `*.hosts` files as additional host files, so feel free to put any additional stuff there.

## UniFi USG

* Go to Settings -> Networks -> LAN
* Set "DHCP Name Server" to manual and enter the IP of the machine running unifi-dns (and some fallback servers)
