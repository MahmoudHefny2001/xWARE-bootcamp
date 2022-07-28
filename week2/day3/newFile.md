# Exercise 1

## Normalize Student and Professor

```

create table if not exists student_phones(
	id serial primary key,
	f_Phone int not null,
	l_Phone int not null,
	
	student_id int references student(id)
);



<!----
 id | f_phone | l_phone | student_id 
----+---------+---------+------------
  1 |  654365 |  124578 |          1
  2 |   56432 |  789456 |          2
  3 |   84654 |  147852 |          3
  4 |   54532 |  963258 |          4
  5 |    5612 |  475829 |          5
  6 |   56122 |  456287 |          8
  7 |   56432 |  971355 |         10
  8 |  656532 |  001144 |         11
--->



create table if not exists professor_Name(
	id serial primary key,
	f_Name varchar(40),
	l_Name varchar(40),
	
	professor_id int references professor(id)
);




<!----
 id | f_name  | l_name  | professor_id 
----+---------+---------+--------------
  1 | Hamada  | Hassan  |            1
  2 | Hossam  | Ali     |            2
  3 | Mustafa | Hussein |            3
  4 | Khaled  | Omar    |            4
  5 | Ahmed   | Ali     |            5
  6 | Mahmoud | Ismael  |           11
  7 | Amr     | Mustafa |           13
------>

# Exercise 2


create table if not exists person(
	personId serial primary key,
	lastName  varchar(50),
	firstName varchar(50)
);

<!------
{
 personid | lastname | firstname 
----------+----------+-----------
        1 | Wang     | Allen
        2 | Alice    | Bob
        3 | Smith    | Lee
}	
------>


create table if not exists address(
	addressId serial primary key,
	city varchar(40),
	state varchar(40),
	
	person_id int references person(personId)
);


<!------
{
 addressid |     city      |   state    | personid 
-----------+---------------+------------+----------
         1 | New York City | New York   |        2
         2 | Leetcode      | California |        1
}
---->

## INSERT steps


`INSERT INTO person(lastName, firstName) VALUES('Wang', 'Allen'), ('Alice', 'Bob');`

`INSERT INTO address(personId, city, state) VALUES(2, 'New York City', 'New York'), (1, 'Leetcode', 'California');`

`INSERT INTO person(lastName, firstName) VALUES('Smith', 'Lee');`



## JOIN steps

`SELECT person.firstName, lastName, city, state FROM person FULL OUTER JOIN address ON address.personId = person.personId;`

<!-------
[
 firstname | lastname |     city      |   state
-----------+----------+---------------+------------
 Bob       | Alice    | New York City | New York
 Allen     | Wang     | Leetcode      | California
 Lee       | Smith    |               | 
]
---->

