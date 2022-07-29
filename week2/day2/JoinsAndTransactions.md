# Create New Transaction

- begin;

## Insert commands In Professors and Students tables

- INSERT INTO professor() VALUES();

- INSERT INTO student() VALUES();



## Select commands of professors and students

- SELECT * FROM professor;
- SELECT * FROM student;


`When i open another session and select all the Professors and Students, the data was retrieved in the first session before i create the New Transaction will be shown in the second session`




## Delete commands of Professors with salary greater than 2000

<!--DELETE FROM Professor 
	WHERE SALARY > 20000; -->


`Nothing will change when i try to select all Professors and Students in the other session`


## Rollback command

ROLLBACK;

`Nothing will change when i try to select all Professors and Students in the other session`


## Commit command

COMMIT;

`When i select all professors and students in the other session after i commit in the first session the same result will be shown in the other session as i select all professors and students in the first session`


## Insert commands in professors table with a duplicated id

INSERT INTO Professor() VALUES();

`I will get an error when i try to insert commands in professors table with a duplicated id which is "duplicate key value violates unique constraint "professor_pkey""`


## Insert commands in student table with a duplicated id

INSERT INTO Student() VALUES();

`I will get an error when i try to insert commands in professors table with a duplicated id which is "current transaction is aborted, commands ignored until end of transaction block""`



## Final Commit command in the exercise

`When i commit, it shows me "ROLLBACK" message`


## Final Rollback command in the exercise
`When i rollback, it shows me a Warning which is "there is no transaction in progress" and Rollback work in the next line`


--------------------------------------------------



# "Join" exercise

- Select subject.id, name, code, duration from subject INNER JOIN course ON course.subject_id = subject.id;

- SELECT subject.id, name, code, duration, f_name, l_name FROM subject INNER JOIN course ON course.subject_id = subject.id LEFT JOIN professor ON course.professor_id = professor.id;

- SELECT student.id, f_name, l_name, line_1Address, Line_2Address FROM student INNER JOIN student_address ON student_address.student_id = student.id INNER JOIN address ON student_address.address_id = address.id;

- SELECT student.id, f_Name, l_Name, duration from student INNER JOIN course_enrolment ON course_enrolment.student_id = student.id INNER JOIN course ON course.id = course_enrolment.course_id;
