#!/usr/bin/env python3
import os
import requests


baseurl = os.environ.get('UNIFI_BASEURL', 'https://unifi:8443')
username = os.environ.get('UNIFI_USERNAME')
password = os.environ.get('UNIFI_PASSWORD')
site = os.environ.get('UNIFI_SITE', 'default')

def get_clients():
    s = requests.Session()
    r = s.post(f'{baseurl}/api/login', json={'username': username, 'password': password}, verify=False)
    r.raise_for_status()
    r = s.get(f'{baseurl}/api/s/{site}/rest/user', verify=False)
    r.raise_for_status()
    return sorted(r.json()['data'], key=lambda i: i.get('fixed_ip', ''))

for c in get_clients():
    if 'name' in c and 'fixed_ip' in c:
        print(c['fixed_ip'], c['name'])

