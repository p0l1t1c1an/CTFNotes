#! /usr/local/bin/python3

import base64

plaintext = b'{"showpassword":"no","bgcolor":"#ffffff"}'
ciphertext64 = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=='
ciphertext = base64.b64decode(ciphertext64)

if len(plaintext) == len(ciphertext):
    for i in range(0, len(plaintext)):
        print('{} -> {}\tKey == {}'.format(hex(plaintext[i]), hex(ciphertext[i]), hex(plaintext[i] ^ ciphertext[i])))

