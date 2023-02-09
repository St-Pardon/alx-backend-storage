# 0x00. MySQL advanced


## Tasks

### [0. We are all unique!](./0-uniq_users.sql)

Write a SQL script that creates a table users following these **requirements:**

- With these attributes:
    - `id`, `integer`, never null, `auto increment` and `primary key`
    - `email`, string (255 characters), `never null` and `unique`
    - `name`, string (255 characters)
- If the table already exists, your script should not fail
Your script can be executed on any database
- Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application
```bash
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
```


[1. In and not out](./1-country_users.sql)

Write a SQL script that creates a table users following these **requirements:**

- With these attributes:
    - `id`, `integer`, `never null`, `auto increment` and `primary key`
    - `email`, `string` (255 characters), `never null` and `unique`
    - `name`, `string` (255 characters)
    - `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
- If the table already exists, your script should not fail
- Your script can be executed on any database
```bash
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ 
Repo:
```
   
[2. Best band ever!](./2-fans.sql)

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

- Import this table dump: [metal_bands.sql.zip](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230209%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230209T133110Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=22f68f617d65635f5f5e972fbc3c5410e0736a5876687c617515d94ef95e1127)

- Column names must be: `origin` and `nb_fans`
- Your script can be executed on any database
- Context: Calculate/compute something is always power intensive… better to distribute the load!
```bash
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 
```
[3. Old school band](./3-glam_rock.sql)

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

**Requirements:**

- Import this table dump: [metal_bands.sql.zip](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230209%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230209T133110Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=22f68f617d65635f5f5e972fbc3c5410e0736a5876687c617515d94ef95e1127)
- Column names must be: `band_name` and `lifespan` (in years)
- You should use attributes `formed` and `split` for computing the `lifespan`
- Your script can be executed on any database
```bash
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$ 
```