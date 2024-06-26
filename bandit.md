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