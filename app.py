#!/usr/bin/env python3

__author__ = "viperDavid"

import requests

web = requests.get('http://www.google.com')

#print(web.content)


print("status code is {}".format(web.status_code))