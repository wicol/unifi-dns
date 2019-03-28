#!/usr/bin/env python3
import os
from unifi import API as UnifiAPI


baseurl = os.environ.get('UNIFI_BASEURL', 'https://unifi:8443')
username = os.environ.get('UNIFI_USERNAME')
password = os.environ.get('UNIFI_PASSWORD')

api = UnifiAPI(
    username=username,
    password=password,
    baseurl=baseurl,
    verify_ssl=False
)
api.login()
device_list = api.list_clients(order_by='ip')
for device in device_list:
    if 'name' in device and 'fixed_ip' in device:
        print(device['fixed_ip'], device['name'])
api.logout()

