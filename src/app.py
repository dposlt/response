#!/usr/bin/env python3

__author__ = "viperDavid"

import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.johnlewis.com/john-lewis-partners-warner-faux-leather-office-chair/p1891692', verify=False)
content = web.content

soup = BeautifulSoup(content, "html.parser")
element = soup.find("p",{"class":"price price--large"})

print(element.text.strip())
# https://www.johnlewis.com/john-lewis-partners-warner-faux-leather-office-chair/p1891692
# <p class="price price--large">£150.00</p>

if (web.status_code) == 200:
    print("status code is {}".format(web.status_code))
    print(element.text)