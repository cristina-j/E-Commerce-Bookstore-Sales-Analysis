-- The data I have created has already been clean. I want my data to reflect real-world data, so I have updated and inserted data discrepancies to the three tables: Books, Customers, and Purchases to reflect that --

-- Books Table: I have updated entries to NULL in the Genre column --
UPDATE Books 
SET Genre = 'NULL'
WHERE Book_ID IN (3, 6, 29, 45, 79, 123);

-- Books Table: I have updated entries in the Format column --
UPDATE Books 
SET Format = 'paper back'
WHERE Book_ID IN (10, 20, 60, 75);

UPDATE Books
SET format = 'Paper back'
WHERE Book_ID IN (15, 22, 46);

UPDATE Books
SET Format = 'ebook'
WHERE BOOK_ID IN (2, 25, 72);

-- Books Table: Duplicating book titles --

INSERT INTO Books (Book ID, Title, Author, Genre, Price, Published Date, Format)
SELECT  
	130,
	Title, 
	Author, 
	Genre, 
	Price, 
	Published Date, 
	Format
From Books
WHERE [Book ID] IN (123);

-- Customers Table: Adding NUll values --

UPDATE Customers 
SET Email = NULL
WHERE Customer_ID IN (1, 10, 16, 35);

UPDATE Customers
SET Location = NULL 
WHERE Customer_ID IN (13, 23, 45);

-- Customers Table: Duplicating customers --

INSERT INTO Customers (Customer_ID, First_Name, Last_Name, Email, Location)
SELECT 
51, 
First_Name,
Last_Name,
Email, 
Location
From Customers 
WHERE Customer_ID IN (21, 22);

-- Purchases Table: Adding NULL values -- 
UPDATE Purchases 
SET Purchases_Date = '2023-06-01'
WHERE Purchases_ID IN (2);

UPDATE Purchases 
SET Purchase_Date = '2024-01-01'
WHERE Purchase_ID IN (29);

-- Updating the Format column in every instance where 'Kindle Edition is presented

UPDATE Books
SET Format = 'eBook'
WHERE Format ='Kindle Edition';

-- Chaning values that were written as ‘ebook’ to ‘eBook’ --

UPDATE Books
SET Format = 'eBook'
WHERE Format = 'ebook';

-- Changing book titles that did not have the proper format associated with it -- 

UPDATE Books
SET Format = 'Paperback'
WHERE Book_ID IN (8, 10, 11, 14, 15, 20, 26, 27, 35, 36, 56, 60, 64, 65, 67, 69, 74, 75, 76, 77,  78, 81, 86, 88, 91, 93, 99, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 126);

UPDATE Books
SET Format = 'eBook'
WHERE Book_ID IN (9, 21, 49, 58, 101, 107);

UPDATE Books 
SET Format = 'Hardcover'
WHERE Book_ID IN (83, 90, 94, 96);







