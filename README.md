# Book-Insights-Project

A personal data analyst project that uses a fictional bookstore database to showcase my skills in Python, SQL, data cleaning, and analysis.

## Project Description

This project simulates a small independent bookstore using real book data of all the books I have read that I have tracked on Goodreads and fake customers and purchase data generated with Python.

The SQLite database (`Book Nook.db`) contains the `Books`, `Customers`, and `Purchases` tables, all created using Python. The `Book_Insights_Project.sql` file includes manually written SQL code to recreate the same schema and structure, showcasing proficiency in both programming and manual database design.

I created:

- A clean database that includes the books, customers, and purchases table
- SQL tables created both manually and using Python
- Data quality testing and error simulation to mimic real-world inconsistencies
- Future plans for analyzing trends in book purchases, genres, and customer behavior

## Files 

- `Book_Nook.db`: This is the SQLite database generated using Python. It contains three clean tables: Books, Customers, and Purchases. To explore the contents, download the file and open it using a database browser such as DB Browser for SQLite or query it directly using Python or SQL tools.
- `Book_Insights_Project.sql`: This file is a SQL script to manually recreate the same three tables and insert sample data (same in the Book_Nook.db), showcasing knowledge of raw SQL.
- `Book_Nook_Database.py`: This is a Python script that creates the clean Book_Nook database, including data extraction, transformation, and table creation.
- `Goodreads_Library_Export`: This is raw Goodreads export of all the books I have read. It's used as the starting dataset

## Tools & Technologies

- Python (Pandas, SQLite, Faker)
- SQL (SQLite + MySQL)
- GitHub for version control
