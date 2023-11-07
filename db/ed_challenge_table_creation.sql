CREATE TABLE STUDENTS(
    student_id serial PRIMARY KEY,
    f_name text NOT NULL,
    i_name text NOT NULL)
    dob date;

CREATE TABLE TEACHERS(
    teacher_id serial PRIMARY KEY,
    teacher_name text NOT NULL);

CREATE TABLE SUBJECTS(
    subject_id serial PRIMARY KEY, 
    subject_name text NOT NULL, 
    teacher_id integer NOT NULL,
    FOREIGN KEY(teacher_id) REFERENCES TEACHERS(teacher_id) ON DELETE SET NULL);

CREATE TABLE ENROLLMENTS(
    enrollment_id serial PRIMARY KEY,
    student_id integer NOT NULL, 
    subject_id integer NOT NULL, 
    enrollment_date date DEFAULT CURRENT_DATE,
    FOREIGN KEY(student_id) REFERENCES STUDENTS(student_id) ON DELETE CASCADE,
    FOREIGN KEY(subject_id) REFERENCES SUBJECTS(subject_id) ON DELETE CASCADE);