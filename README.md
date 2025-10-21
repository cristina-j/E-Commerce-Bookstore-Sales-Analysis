# Book-Insights-Project

The Book Insights Project is a data analytics case study built around a fictional online bookstore inspired by my personal reading data from 2024–2025. The goal of this project is to simulate how a real-world data analyst might use data analysis to uncover insights that drive better business decisions in the retail and e-commerce industry.


## Business Problem

A local online bookstore noticed stagnant sales growth and declining engagement among repeat customers. They wanted to understand which genres and authors drive the most purchases, how different book formats perform (paperback, eBook, hardcover), and how customer preferences shift over time.


## Proposed Solution
To address this, I created a fictional relational database that models real bookstore operations. I developed tables for books, customers, and purchases, then used SQL to analyze trends in spending, genre popularity, and format preferences. By combining data cleaning, querying, and visualization, I transformed raw transactional data into actionable insights a small business could realistically use to guide inventory, pricing, and marketing decisions.


## Updates Made to Files
- `Book_Nook_Database.py`: Added a few lines so that the genre column is automatically assigned based on the author.
- `Book_Nook.db`: Updated the Format column with correct values:
    - 'Kindle Edition' --> 'eBook', 'ebook' --> 'eBook',
    - Book titles that should be 'Paperback' or 'Hardcover' but were not
    - Corrections made to invalid data (Page Count for row 63 was 0, but updated it to 196)
 

## Explanation of Files 

- `Book_Nook.db`: This is the SQLite database generated using Python. It contains three clean tables: `Books`, `Customers`, and `Purchases`. To explore the contents, download the file, and open it using a database browser such as DB Browser for SQLite (like I did) or query it directly using Python or SQL tools.
- `Book_Nook.sql`: This file is a SQL script to manually recreate the same three tables and insert sample data (same in the Book_Nook.db), showcasing knowledge of raw SQL.
- `Book_Nook_Database.py`: This is a Python script that creates the clean `Book_Nook_Database`, including data extraction, transformation, and table creation.
- `Goodreads_Library_Export`: This is the raw Goodreads export of all the books I have read. It's used as the starting dataset.
- `Book_Nook_Dataset.py`: This is a Python script that reads the clean csv files for the `Books`, `Customers`, and `Purchases` tables and puts them into one Excel file called `Book_Nook_Dataset.csv`
- `Book_Nook_Dataset.csv`: Excel file with clean datasets
- `Data_Discrepancies.sql`: Highlights intentional discrepancies to reflect real-world data and to showcase my skill in cleaning data using SQL.

## Tools & Technologies

- Python (Pandas, SQLite, Faker)
- SQL (SQLite + MySQL)
- GitHub for version control
