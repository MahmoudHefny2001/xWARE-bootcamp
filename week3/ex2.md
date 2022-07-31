SQL
```
CREATE TABLE IF NOT EXISTS logins(
	user_id int,
	time_stamp date,
    PRIMARY KEY (user_id, time_stamp)
);
```
```
- insert into logins(user_id, time_stamp) VALUES (1, '2020-06-30 15:06:07');
- insert into logins(user_id, time_stamp) VALUES (2, '2021-04-21 14:06:06');
- insert into logins(user_id, time_stamp) VALUES (3, '2019-03-07 00:18:15');
- insert into logins(user_id, time_stamp) VALUES (4, '2020-02-01 05:10:53');
- insert into logins(user_id, time_stamp) VALUES (5, '2020-12-30 00:46:50');
- insert into logins(user_id, time_stamp) VALUES (6, '2020-01-16 02:49:50');
- insert into logins(user_id, time_stamp) VALUES (1, '2019-08-25 07:59:08');
- insert into logins(user_id, time_stamp) VALUES (1, '2019-07-14 09:00:00');
```


# SELECT * FROM logins ;

```
user_id | time_stamp
---------+------------
       1 | 2020-06-30
       2 | 2021-04-21
       3 | 2019-03-07
       4 | 2020-02-01
       5 | 2020-12-30
       6 | 2020-01-16
       1 | 2019-08-25
       1 | 2019-07-14
(8 rows)
```



# select user_id,
        - max(time_stamp)
               - as last_stamp from Logins
                  -WHERE time_stamp >= '2020-01-01'
                      - and time_stamp < '2021-01-01'
                               - group by user_id ;
				
```				
 user_id | last_stamp
---------+------------
       1 | 2020-06-30
       4 | 2020-02-01
       5 | 2020-12-30
       6 | 2020-01-16
(4 rows)
```
