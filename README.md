# Book-Insights-Project

The Book Insights Project is a data analytics case study built around a fictional online bookstore inspired by my personal reading data from 2024–2025. The goal of this project is to simulate how a real-world data analyst might use data analysis to uncover insights that drive better business decisions in the retail and e-commerce industry.

This analysis focuses on the first six months of 2025, providing an early look at revenue trends, customer engagement, and sales performance across genres, formats, and authors. 


## Business Problem

A local online bookstore noticed slower sales in early 2025. They wanted to understand which genres and authors drive the most purchases, how different book formats perform (paperback, eBook, hardcover) with their customers, and what monthly sales trends reveal about their customers behavior in the first half of the year.


## Proposed Solution
To address this, I created a fictional relational database that models real bookstore operations. I developed tables for books, customers, and purchases, then used SQL to analyze trends in spending, genre popularity, and format preferences. By combining data cleaning, querying, and visualization, I transformed raw transactional data into actionable insights a small business could realistically use to guide inventory, pricing, and marketing decisions.

## Results and Business Recommendation
Insights from the first six months of 2025 show that Romance and its subgenre dominates both the sales and revenue, confirming strong customer loyatly and demand in this genre. Paperbacks lead in overall purchases, while eBooks perform well among price-conscious readers. Hardcovers are high in price, but low in sales and revenue which shows that there can be a chance for it to be suited for premium offerings. Contemporary and Literary Fiction performs lower than other genres which highlights areas for strategic promotion. Considering that January saw the most in sales and revenue, it can be said that there was a post-holiday dip in sales followed by steady performnce through mid-year which suggests room for engagement-driven campaigns to sustain momentum and get customers engaged with the bookstore again.

<img width="788" height="584" alt="Screenshot 2025-10-21 at 6 02 50 PM" src="https://github.com/user-attachments/assets/dc722c90-0c01-47e8-b99d-6d646dbd78d4" />



## Tools & Technologies

- Python (Pandas, SQLite, Faker)
- SQL (SQLite + MySQL)

## Explanation of Files 

- `Book_Nook.db`: This is the SQLite database generated using Python. It contains three clean tables: `Books`, `Customers`, and `Purchases`. To explore the contents, download the file, and open it using a database browser such as DB Browser for SQLite (like I did) or query it directly using Python or SQL tools.
- `Book_Nook.sql`: This file is a SQL script to manually recreate the same three tables and insert sample data (same in the Book_Nook.db), showcasing knowledge of raw SQL.
- `Book_Nook_Database.py`: This is a Python script that creates the clean `Book_Nook_Database`, including data extraction, transformation, and table creation.
- `Goodreads_Library_Export`: This is the raw Goodreads export of all the books I have read. It's used as the starting dataset.
- `Book_Nook_Dataset.py`: This is a Python script that reads the clean csv files for the `Books`, `Customers`, and `Purchases` tables and puts them into one Excel file called `Book_Nook_Dataset.csv`
- `Book_Nook_Dataset.csv`: Excel file with clean datasets
- `Data_Discrepancies.sql`: Highlights intentional discrepancies to reflect real-world data and to showcase my skill in cleaning data using SQL.

## Updates Made to Files
- `Book_Nook_Database.py`: Added a few lines so that the genre column is automatically assigned based on the author.
- `Book_Nook.db`: Updated the Format column with correct values:
    - 'Kindle Edition' --> 'eBook', 'ebook' --> 'eBook',
    - Book titles that should be 'Paperback' or 'Hardcover' but were not
    - Corrections made to invalid data (Page Count for row 63 was 0, but updated it to 196)
