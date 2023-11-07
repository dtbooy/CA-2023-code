/* 
Data Manipulation Challenge
Challenge uses coder_academy database,
*/


--Insert 5 rows in the students table,  
INSERT INTO students(f_name, i_name, dob, email) VALUES
    ('Jessica', 'Jones', '2001-03-07', 'jj@CoderA.edu.au'),
    ('Peter', 'Parker', '1995-01-07', 'pp@CoderA.edu.au'),
    ('Clark', 'Kent', '2000-07-07', 'ck@CoderA.edu.au'),
    ('Waynes', 'World', '1992-08-02', 'ww@CoderA.edu.au'),
    ('Huge', 'Janus', '1985-12-30', 'HJ@CoderA.edu.au');    
--3 rows in teachers,
INSERT INTO teachers(f_name, l_name) VALUES
    ('Patrick', 'Spongebob'),
    ('NEO', 'Anderson'),
    ("Barry", "Moore");
-- 4 rows in subjects 
INSERT INTO subjects(subject_name, teacher_id) VALUES
    ('Maths', 1),
    ('Hope', 2),
    ('Lunch', 1),
    ('Morning Tea', 2),
    ('Software Development', 1);
-- and 10 rows in enrolments.
INSERT INTO enrollments(student_id, subject_id) VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 2),
    (3, 3),
    (4, 4),
    (4, 2),
    (5, 1),
    (5, 3);

--Update one student's date of birth
UPDATE students
SET dob = '2015-12-30'
WHERE l_name = 'World' and f_name = 'Waynes';

--Add some data into the database


-- Update the 'Software Development' subject to Programming.
UPDATE subjects
set subject_name = 'Programming'
WHERE subject_name = 'Software Development';

-- Delete enrollments with enrollment_id 1 and 2 (In one command).
DELETE FROM enrollments
WHERE enrollment_id = 1 OR enrollment_id = 2;

-- Delete student with id 3 and check what happens with their enrolments
SELECT * FROM enrollments; 

DELETE FROM students
WHERE student_id = 3

SELECT * FROM enrollments;
-- Spoiler delete from students cascaded to delete enrolment records for student 3


/*
Simple queries challenge
Write the SQL queries that retrieve the following data: (if the columns are not specified retrieve all of them)
*/

--Show all the teachers.
select * from teachers;

---Show the subject's different areas.
SELECT DISTINCT area from subjects;

--Show the subject names alphabetically ordered.
Select subject_name from subjects order by subject_name;

--Show the first name, last name and dob of birth of the students starting with the youngest.
Select f_name, l_name, dob from students order by dob DESC;

--Show the enrollments of the students 4 and 5
select * from enrollments where student_id = 4 or student_id = 5;

--Show the email of students who were born in the 90s decade
Select email from students where dob BETWEEN '1/1/1990' AND '1/1/2000';

--Show the students whose last name starts with an A. 
select * from students where l_name LIKE 'A%';