# Books and Things
# What this script does:
# This script will create a Books table from my Goodreads csv file
# This script will create a fake Customers and Purchase table using the Faker function in Python
# At the end, this script will save all three of the tables in a database named "Book_Nook"
# There are comments for each table as they are being created to understand how they are created


# What I am importing to create the tables

import sqlite3
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta, date

# Every time I ran this script, it would create new customers and purchases data.
# I want to be able to run this script multiple times and keep the data already generated
random.seed(50)
Faker.seed(50)

# This connects to the SQLite database
connection = sqlite3.connect('Book_Nook.db')
cursor = connection.cursor()

# Creating the Books Table
# Python is going to read my Goodreads csv file
df = pd.read_csv ('goodreads_library_export.csv')

# I want to create a new dataframe where I only have specific columns I want from the original csv while not making any
# changes to the original csv
df_books = df[['Book Id', 'Title', 'Author', 'Binding', 'Number of Pages', 'Year Published']].copy()

# I want some of the columns name in the new csv file to be different from the original file
df_books.columns = ['Book ID', 'Title', 'Author', 'Format', 'Page Count', 'Published Year']

# The IDs in the Book ID column are long, and I want to change it so it is shorter starting from the number 1
df_books['Book ID'] = range(1, len(df_books) + 1)

# I realized that the Genre column is empty for each book, and when I make changes to it and save those changes, 
# the next time I run the script, those changes disappear
# I need to assign books a genre using a dictionary based on the authors because there are less authors to books
# This will also default to Romance if author is not found in the dictionary
author_genre = {
    'B.K. Borison': 'Romance',
    'Harper L. Woods': 'Paranormal Romance',
    'Aurora Ascher': 'Paranormal Romance',
    'Penelope Sky': 'Dark Romance',
    'J.T. Geissinger': 'Dark Romance',
    'Ana Huang': 'Romance',
    'Kaylie Smith': 'Fantasy',
    'Lyla Sage': 'Romance',
    'Joya Goffney': 'Romance',
    'Elsie Silver': 'Romance',
    'Sierra Simone': 'Dark Romance',
    'Ali Hazelwood': 'Romance',
    'Lexi C. Foss': 'Paranormal Romance',
    'N.J. Gray': 'Romance',
    'Rebecca Yarros': 'Romantasy',
    'C.M. Nasosta': 'Paranormal Romance',
    'Emily McIntire': 'Romance',
    'Grace McGinty': 'Romance',
    'G.M. Fairy': 'Paranormal Romance',
    'S.J. Tilly': 'Dark Romance',
    'Jessica  Peterson': 'Romance',
    'Navessa Allen': 'Romance',
    'Emily Rath': 'Romance',
    'Jaymin Eve': 'Paranormal Romance',
    'Cate C. Wells': 'Paranormal Romance',
    'Jenika Snow': 'Romance',
    'Sara Cate': 'Dark Romance',
    'Sadie Kincaid': 'Romance',
    'Jere Anthony': 'Romance',
    'Hannah Grace': 'Romance',
    'Holly Wilde': 'Paranormal Romance',
    'Mallory Marlowe':	'Romance',
    'Lily Mayne': 'Paranormal Romance',
    'Ashley Poston': 'Romance',
    'Tate McKirk': 'Paranormal Romance',
    'Siggy Shade': 'Paranormal Romance',
    'Rebecca J. Caffery': 'Romance',
    'Ivy Fairbanks': 'Romance',
    'Alexis Hall': 'Romance',
    'Abby Jimenez': 'Romance',
    'Jay Kristoff':	'Fantasy',
    'Jessica Joyce': 'Romance',
    'Tomi Adeyemi': 'Fantasy',
    'M. James': 'Dark Romance',
    'Christina Lauren': 'Romance',
    'Lauren Asher':	'Romance',
    'Sharon C. Cooper': 'Romance',
    'Olivia Atwater': 'Romance',
    'Mia Sheridan': 'Romance',
    'Carian Cole': 'Romance',
    'Jennifer L. Armentrout': 'Romantasy',
    'Sarah J. Maas': 'Romantasy',
    'Hanya Yanagihara': 'Literary Fiction',
    'Danielle L. Jensen': 'Romantasy',
    'Carissa Broadbent': 'Romantasy',
    'Tracy Wolff': 'Paranormal Romance',
    'Alexandria Bellefleur': 'Romance',
    'Madeline Miller': 'Fantasy',
    'Elizabeth Acevedo': 'Romance',
    'Jasmine Guillory':	'Romance',
    'Safia Elhillo': 'Contemporary Fiction',
    'Jen Wang': 'Graphic Novel',
    'Alexis Daria': 'Romance',
    'Bolu Babalola': 'Romance',
    'K.M. Moronova': 'Dark Romance',
    'Alexa  Martin': 'Romance',
    'Tiffany D. Jackson': 'Contemporary Fiction',
    'Elle Kennedy':	'Romance',
    'Morgan Bridges': 'Dark Romance',
    'Tessa Bailey': 'Romance',
    'Helen Hoang': 'Romance',
    'Lucy Score': 'Romance',
    'John Green': 'Romance',
    'V.E. Schwab': 'Fantasy',
    'Emily Henry': 'Romance',
    'Casey McQuiston': 'Romance'
}

df_books['Genre'] = df_books['Author'].apply(lambda author: author_genre.get(author.strip(), 'Romance'))


# I want to add another column called Price and create random prices for each book between $5.99 and $29.99
min_price = 5.99
max_price = 29.99

# This will create random prices for each entry in the dataframe and round them to 2 decimal places
df_books['Price'] = np.round(np.random.uniform(min_price, max_price, size=len(df_books)), 2)

# I want to change the order of the columns and include the two new columns I've added
df_books = df_books [['Book ID', 'Title', 'Author', 'Genre', 'Published Year', 'Page Count', 'Format', 'Price']]

# This is going to create the table in SQLite since it is connected
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Book_ID INTEGER PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Genre TEXT,
        Price REAL,
        Published_Date INTEGER,
        Format TEXT
    )
''')






# CREATING THE CUSTOMERS TABLE
# I want to create a Customers table with fake data so that it can be added to the database
# I want to add fake locations for the customers
# These are the 50 states that will be randomized in the table
fake = Faker()
us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

# I want to create fake data for 50 customers
num_customers = 50
customers = []
genders = ['Male', 'Female']

# This will be a for loop that will loop through the customers and create fake data for them
for customer_id in range (1, num_customers + 1):
    gender = random.choice(genders)
    if gender == 'Male':
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
    last_name = fake.last_name()
    number = random.randint(10, 99)
    email = f"{first_name.lower()}{last_name.lower()}{number}@gmail.com"
    phone_number = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    state = random.choice(us_states)
    age = random.randint(18, 80)
    customers.append((customer_id, first_name, last_name, email, phone_number, age, gender, state))

df_customers = pd.DataFrame(customers, columns=['Customer_ID', 'First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Age', 'Gender', 'State'])

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        Customer_ID INTEGER PRIMARY KEY,
        First_Name TEXT,
        Last_Name TEXT,
        Email TEXT,
        Phone_Number TEXT,
        Age INT,
        Gender TEXT,
        State TEXT
    )
''')





# CREATING THE PURCHASES TABLE
# This table will connect with the Books and Customers table because it will have Book ID and Customer_ID presented

# I want to create fake data for the purchases table so it can be added to the database
number_of_purchases = 50
purchases = [] # This is where the data will be stored
start_date = datetime(2025, 1, 1) # Purchases starting in the beginning of January
end_date = datetime(2025, 6, 30) # Purchases ending at the end June

# This will be a for loop that will loop through the purchases and create fake data for it
for Purchase_ID in range (1, number_of_purchases + 1):
    Customer_ID = random.randint(1, number_of_purchases)
    Book_ID = random.randint(1, len(df_books)) # According to how many Book IDs there are in the Books table
    Quantity = random.randint(1, 3) # Customers are limited to three books

    # This will grab the prices in the Books tab and connect it to the Purchases table
    Price = df_books.at[Book_ID - 1, 'Price']  # book_id - 1 to match dataframe index
    Purchased_Date = fake.date_between(start_date, end_date)
    Total_Amount = round(Price * Quantity, 2)

    purchases.append((Purchase_ID, Customer_ID, Book_ID, Quantity, Purchased_Date, Total_Amount))

df_purchases = pd.DataFrame(purchases, columns=['Purchase_ID', 'Customer_ID', 'Book_ID', 'Quantity', 'Purchased_Date', 'Total_Amount'])


# Delete existing table to avoid conflict
# Had to do this because I kept getting an error in Termina stating that the Purchases table already existed
cursor.execute('DROP TABLE IF EXISTS Purchases')

# Recreate with foreign keys
cursor.execute('''
    CREATE TABLE Purchases (
        Purchase_ID INT,
        Customer_ID INT,
        Book_ID INT,
        Quantity INT,
        Purchased_Date TEXT,
        Total_Amount REAL,
        FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
        FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID)
    )
''')


# This is going to insert data into the Books, Customers, and Purchases table
df_books.to_sql('Books', connection, if_exists='replace', index=False)
df_customers.to_sql('Customers', connection, if_exists='replace', index=False)
# Because there are foreign keys in the table, I cannot use 'replace' because Pandas does not know how to create foreign keys. 
# So while the table is created, it is then removed and then Pandas tries to recreate it without foreign keys
df_purchases.to_sql('Purchases', connection, if_exists='append', index=False)

# This will finalize the database
connection.commit()
connection.close()



