/* 
CREATED BY DIRK BOOY
CREATE DATE 2023/11/07
DESCRIPTION: Ed Lesson on SQL INSERT command. 
The database used in this lesson is coder_first_db.
*/

-- basic form of INSERT
INSERT INTO departments (dept_id, dept_name) 
    VALUES (10, 'IT');
/* 
Postgres return: INSERT 0 1
First number is number of failed entries, Second number is number of successful entries
*/

-- Don't need to include column names if using the order defined in the table
INSERT INTO departments VALUES (11, 'marketing');

--if you try to input a foreign key element that is not in the foreign table it will error 
INSERT INTO employees VALUES (1, 'Susan', 'McDonald', '12/03/1995', 157, 'Project manager'); -- error output
INSERT INTO employees VALUES (1, 'Susan', 'McDonald', '12/03/1995', 10, 'Project manager');

--Multiple records can be  entered in a single line:
INSERT INTO PROJECTS(proj_id, proj_name, proj_location) 
VALUES 
    (12, 'MTE Website', 'Melbourne'),
    (14, 'Slip&Co App', 'Online'),
    (17, 'New Gems Website', 'Melbourne'),
    (1, 'Fun with Bonus', 'Brisbane'),
    (2, 'New Projects Website', 'online'); 
--NOTE: location has default value of "online", however must be included as all lists in command must be same length

-- Seed some more random shit
INSERT INTO departments VALUES 
(12, 'Sales'),
(13, 'Service Center'),
(14, 'HR'),
(15, 'Management');

INSERT INTO employees VALUES
(3, 'Dirk', 'Booy', '12/03/54', 15, 'Overlord'),
(4, 'Gary', 'Xandier', '2004-03-23', 12, 'Smith'),
(5, 'Jason', 'Asano', '19930501', 12, 'Loud Mouth'),
(6, 'Farah', 'Huren', '19830223', 13, 'Lava Cannon');
-- Note: Dates can be entered in basically any way - best practice is YYYY-MM-DD. This avoids stupid US dates messing you up

--Note: Don't add an entry for serial PRIMARY KEYS - its gets added automatically
-- This means you need to exclude it in the column selection - can't jsut add values
INSERT INTO hour_assignments(project_id, employee_id, hours) VALUES
(1, 3, 20.5),
(14, 2, 40),
(17, 1, 25),
(2, 6, 10.25),
(12, 5, 0.5);


DELETE FROM table_name WHERE condition(s)
-- NEED to specify conditions or it will delete every entry in table eg:
DELETE FROM HOUR_ASSIGNMENTS;
-- Deletes all records in hours assignments

-- WHERE Works the same as with queries can use =,<,>, between, like,and,or ,etc
DELETE FROM DEPARTMENTS
WHERE dept_name = 'Operations';


UPDATE table_name 
SET attr_to_update = updated_value
WHERE condition(s)
-- NEED to specify conditions or it will update every record in table eg:
UPDATE EMPLOYEES 
SET department_id = 12;
-- this updates all employees records to have teh department_id of 12 

-- WHERE Works the same as with queries can use =,<,>, between, like,and,or ,etc
UPDATE EMPLOYEES 
SET department_id = 11 
WHERE emp_id = 5;

