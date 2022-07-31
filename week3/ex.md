# \c person

SQL 

```
CREATE TABLE IF NOT EXISTS person(
	ID serial primary key,
	email varchar(100)
);
```
# \d person

```
                                  Table "public.person"
 Column |          Type          | Collation | Nullable |              Default
--------+------------------------+-----------+----------+------------------------------------
 id     | integer                |           | not null | nextval('person_id_seq'::regclass)
 email  | character varying(100) |           |          |
Indexes:
    "person_pkey" PRIMARY KEY, btree (id)
```

- INSERT INTO person(email) VALUES('hefny4@gmail.com');
- INSERT INTO person(email) VALUES('fakeAccount@gmail.com');
- INSERT INTO person(email) VALUES('fakeAccount@gmail.com');
- INSERT INTO person(email) VALUES ('john5@gmail.com');
- INSERT INTO person(email) VALUES ('pop88@gmail.com');
- INSERT INTO person(email) VALUES ('john5@gmail.com');
- INSERT INTO person(email) VALUES ('pop88@gmail.com');

# SELECT lower(email) FROM person;

You are now connected to database "person" as user "postgres".

# SELECT * FROM person;

```
id |         email
----+-----------------------
  1 | hefny4@gmail.com
  2 | fakeAccount@gmail.com
  3 | fakeAccount@gmail.com
  4 | john5@gmail.com
  5 | pop88@gmail.com
  6 | john5@gmail.com
  7 | pop88@gmail.com
(7 rows)
```

 # DELETE FROM person a USING person b WHERE a.id < b.id AND a.email = b.email;


 DELETE 3


# SELECT * FROM person;

```

 id |         email
----+-----------------------
  1 | hefny4@gmail.com
  3 | fakeAccount@gmail.com
  6 | john5@gmail.com
  7 | pop88@gmail.com
(4 rows)

```




