import pandas as pd



# Read each csv file separately into a separate dataframe

df_books = pd.read_csv('Books_Dataset.csv')
df_customers = pd.read_csv('Customers_Dataset.csv')
df_purchases = pd.read_csv('Purchases_Dataset.csv')

# Now I want to create one big Excel file with the three dataframes in separate sheets

with pd.ExcelWriter('Combining_Excel_Files.xlsx', engine='xlsxwriter') as writer:
    df_books.to_excel(writer, sheet_name='Books', index=False)
    df_customers.to_excel(writer, sheet_name='Customers', index=False)
    df_purchases.to_excel(writer, sheet_name='Purchases', index=False)

