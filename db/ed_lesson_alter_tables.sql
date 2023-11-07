-- Add an email column to students that cannot be null.
ALTER TABLE STUDENTS
INSERT COLUMN email text NOT NULL;

-- Rename tachers' name attribute to f_name, and add a l_name column.
ALTER TABLE TEACHERS
RENAME COLUMN full_name 
TO f_name;

ALTER TABLE TEACHERS
INSERT COLUMN l_name varchar(50) NOT NULL;

-- Add an area column to subject where default value is 'Databases'.
ALTER TABLE SUBJECTS
INSERT COLUMN area charvar(50) DEFAULT 'Database';

-- Try to drop SUBJECTS table and comment what happens.
DROP TABLE SUBJECTS;