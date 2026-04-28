-- database: student_database.db

SELECT * 
FROM students
WHERE age > 20;

SELECT first_name
FROM students
WHERE age > 20
ORDER BY first_name ASC;

SELECT lecturer
FROM courses
WHERE lecturer LIKE "Dr.%";

SELECT DISTINCT lecturer, name
FROM courses;

SELECT *
FROM students
WHERE id IN (1, 2, 3 ,4, 5)