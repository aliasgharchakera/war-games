# Bandit War Games

## Passwords and Commands

### Level 0
```bandit0```

```
cat readme
```

### Level 1
```ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If```

```
cat ./-
```

### Level 2
```263JGJPfgU6LtdEvgfWU1XP5yac29mFx```

```
cat 'spaces in this filename'
```

### Level 3
```MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx```

```
cd inhere/

cat ./...Hiding-From-You
```

### Level 4
```2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ```

```
cd inhere/

file ./-file*

cat ./-file07
```

### Level 5
```4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw```

```
cd inhere/

find . -not -executable -type f -size 1033c

cat maybehere07/.file2
```

### Level 6
```HWasnPhtq9AVKe0dmk45nxy20cvUa6EG```

```
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null

cat /var/lib/dpkg/info/bandit7.password
```


### Level 7
```morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj```

```
cat data.txt | grep millionth
```

### Level 8
```dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc```

```
grep . data.txt | sort | uniq -u
```

### Level 9
```4CKMh1JI91bUIZZPXDqGanal4xvAg0JM```

```
grep -a "===*" data.txt
```

### Level 10
```FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey```

```
base64 -d data.txt
```

### Level 11
```dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr```

```
cat data.txt | tr 'a-z' 'n-za-m' | tr 'A-Z' 'N-ZA-M'
```

### Level 12
```7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4```

```
cd /tmp

mktemp -d 

cd /tmp/tmp.XYZ

cp ~/data.txt .

mv data.txt hexdump_data

xxd -r hexdump_data compressed_data

cat compressed_data | head

cat hexdump_data | head

mv compressed_data compressed_data.gz

gzip -d compressed_data.gz

xxd compressed_data

mv compressed_data compressed_data.bz2

bzip2 -d compressed_data.bz2

xxd compressed_data

mv compressed_data compressed_data.gz

gzip -d compressed_data.gz

xxd compressed_data

mv compressed_data compressed_data.tar

tar -xf compressed_data.tar

tar -xf data5.bin

xxd data6.bin

bzip2 -d data6.bin

xxd data6.bin.out

tar -xf data6.bin.out

xxd data8.bin

mv data8.bin data8.gz

gzip -d data8.gz

cat data8
```

### Level 13
```FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn```

```
ls
// sshkey.private is present in the root directory

exit

scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .

chmod 700 sshkey.private

ssh -i sshkey.private bandit13@bandit.labs.overthewire.org -p 2220
```

### Level 14
```sshkey.private``` ```MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS```

```
cat /etc/bandit_pass/bandit14

nc localhost 30000

MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

### Level 15
```8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo```

```
openssl s_client -connect localhost:30001

8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

### Level 16
```kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx```

```
nmap -sV localhost -p 31000-32000

echo kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx | openssl s_client -quiet -connect localhost:31790
```

### Level 17
```sshkey17.private```

```
diff passwords.old passwords.new
```

### Level 18
```x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO```

```
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```

### Level 19
```cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8```

```
ls -la

./bandit20-do id

./bandit20-do ls /etc/bandit_pass

./bandit20-do cat /etc/bandit_pass/bandit20
```

### Level 20
```0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO```

```
echo -n 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO | nc -l -p 1234 &

./suconnect 1234
```

### Level 21
```EeoULMCra2q0dSkYj561DX7s1CpBuOBt```

```
ls -la /etc/cron.d

cat /etc/cron.d/cronjob_bandit22

cat /usr/bin/cronjob_bandit22.sh

cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

### Level 22
```tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q```

```
ls -la /etc/cron.d

cat /etc/cron.d/cronjob_bandit23

cat /usr/bin/cronjob_bandit23.sh

echo I am user bandit23 | md5sum | cut -d ' ' -f 1

cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

### Level 23
```0Zf11ioIjMVN551jX3CmStKLYqjk54Ga```

```
ls -la /etc/cron.d

cat /etc/cron.d/cronjob_bandit24

cat /usr/bin/cronjob_bandit24.sh
```
