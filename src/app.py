#!/usr/bin/env python3

__author__ = "viperDavid"

import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.johnlewis.com/john-lewis-partners-warner-faux-leather-office-chair/p1891692', verify=False)
content = web.content

soup = BeautifulSoup(content, "html.parser")
priceElement = soup.find("p",{"class":"price price--large"})
descriptionElement = soup.find("h1",{"class":"product-header__title"})


# https://www.johnlewis.com/john-lewis-partners-warner-faux-leather-office-chair/p1891692
# <p class="price price--large">£150.00</p>
# <h1 class="product-header__title">John Lewis &amp; Partners Warner Faux Leather Office Chair</h1>
if (web.status_code) == 200:
    print("{}:{}".format(descriptionElement.txt.strip(),priceElement.text.strip()))
else:
    print("status code is {}".format(web.status_code))