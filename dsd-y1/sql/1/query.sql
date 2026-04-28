-- database: chinook.db

SELECT FirstName, LastName
FROM employees
WHERE Title == "IT Staff";

SELECT *
FROM tracks
WHERE MediaTypeId == 3 AND AlbumId < 250;

SELECT FirstName, LastName, Title
FROM employees
WHERE City == "Calgary";

SELECT *
FROM customers
WHERE City == "Boston";

ALTER TABLE artists ADD COLUMN Tracks AS
