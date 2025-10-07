-- What are the most common genres in the bookstore?

SELECT 
	Genre,
	COUNT(*) AS Count
FROM
	Books
GROUP BY
	Genre
ORDER BY 
	Count DESC;



--I notice that some of the prices does not have two numbers after the decimal, so I would need to update the prices whenever I need to query for price. So if I want to see if the query works to change the prices, it would look like this--

SELECT 
	Title,
	printf('%.2f', Price) AS Formatted_Price
FROM 
	Books



-- What are the top 5 most expensive books? --

SELECT 
	Title,
	Author,
	printf('%.2f', Price) AS Formatted_Price
FROM 
	Books
ORDER BY 
	Price DESC
LIMIT 5;



-- What book formats are most used? --

SELECT 
    Format,
    COUNT(*) AS Count
FROM 
    Books
GROUP BY 
    Books 
ORDER BY
    Count DESC;



-- Which books have been purchased the most? --

SELECT 
    b.title, COUNT(*) AS Total_Purchases
FROM 
    Purchases p
JOIN Books b 
ON p.Book_ID = b.Book_ID
GROUP BY 
    b.title
ORDER BY Total_Purchases DESC;



-- Which customers spent the most?--

SELECT 
	c.First_Name || ' ' || c.Last_Name AS Customer_Name,
	printf('%.2f', SUM(p.Total_Amount)) AS Total_Spent
FROM 
    Purchases p
JOIN 
    Customers c 
ON p.Customer_ID = c.Customer_ID
GROUP BY 
	Customer_Name
ORDER BY 
	SUM(p.Total_Amount) DESC;



-- Which customer spent the least? --

SELECT 
	c.First_Name || ' ' || c.Last_Name AS Customer_Name,
	printf('%.2f', SUM(p.Total_Amount)) AS Total_Spent
FROM 
    Purchases p
JOIN 
    Customers c 
ON p.Customer_ID = c.Customer_ID
GROUP BY 
	Customer_Name
ORDER BY 
	SUM(p.Total_Amount) ASC;



-- Who are the customers that have purchased more than once from the store? --

SELECT 
    c.Customer_ID,
    c.First_Name || ' ' || c.Last_Name AS Customer_Name,
    COUNT(p.Purchase_ID) AS Times_Purchased
FROM Purchases p
JOIN Customers c 
ON p.Customer_ID = c.Customer_ID
GROUP BY c.Customer_ID
HAVING COUNT(p.Purchase_ID) > 1
ORDER BY Times_Purchased ASC;



-- What are the names of the books customers bought who have made purchases more than once from the store? --

SELECT 
    c.Customer_ID,
    c.First_Name || ' ' || c.Last_Name AS Customer_Name,
    b.Title AS Book_Title,
    p.Purchase_Date
FROM Purchases p
JOIN Customers c ON p.Customer_ID = c.Customer_ID
JOIN Books b ON p.Book_ID = b.Book_ID
WHERE c.Customer_ID IN (
    SELECT Customer_ID
    FROM Purchases
    GROUP BY Customer_ID
    HAVING COUNT(*) > 1
)
ORDER BY c.Customer_ID, p.Purchase_Date;



-- What format did the customers who have made more than one purchase buy the books in? --

SELECT 
    c.Customer_ID,
    c.First_Name || ' ' || c.Last_Name AS Customer_Name,
    b.Title AS Book_Title,
	b.Format,
    p.Purchased_Date
FROM Purchases p
JOIN Customers c ON p.Customer_ID = c.Customer_ID
JOIN Books b ON p.Book_ID = b.Book_ID
WHERE c.Customer_ID IN (
    SELECT Customer_ID
    FROM Purchases
    GROUP BY Customer_ID
    HAVING COUNT(*) > 1
)
ORDER BY c.Customer_ID, p.Purchased_Date;
