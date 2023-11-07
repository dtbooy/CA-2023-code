-- Add an email column to students that cannot be null.
ALTER TABLE STUDENTS
ADD COLUMN email text NOT NULL;

-- Rename teachers' name attribute to f_name, and add a l_name column.
ALTER TABLE TEACHERS
RENAME COLUMN full_name 
TO f_name;

ALTER TABLE TEACHERS
ADD COLUMN l_name varchar(50) NOT NULL;

-- Add an area column to subject where default value is 'Databases'.
ALTER TABLE SUBJECTS
ADD COLUMN area varchar(50) DEFAULT 'Database';

-- Try to drop SUBJECTS table and comment what happens.
DROP TABLE SUBJECTS;

--Set Default
ALTER TABLE employees 
ALTER COLUMN position
SET DEFAULT 'Software developer'

--Delete a default
ALTER TABLE employees 
ALTER COLUMN position
DROP DEFAULT 'Software developer'

--SEt Not Null
ALTER TABLE employees 
ALTER COLUMN position
SET NOT Null

--Delete Not Null
ALTER TABLE employees 
ALTER COLUMN position
DROP Not null
