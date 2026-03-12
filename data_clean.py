import kagglehub
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("carrie1/ecommerce-data")
print("Path to dataset files:", path)

csv_file = None
for file in os.listdir(path):
    if file.endswith(".csv"):
        csv_file = os.path.join(path, file)
        break

if csv_file:
    print("csv file :", csv_file)
   
    df = pd.read_csv(csv_file, encoding='latin1') # read the csv file into a DataFrame
    print()
    print(df.head())
else:
    print("no results")


#1.basic info about the dataset
print("Basic information about the dataset:\n")
print(f"Dataset shape: {df.shape}")
df.info()

#2.summary statistics for numerical columns
print("Summary statistics for numerical columns:\n")
print(df.describe()) 

#3.handle missing values
print("Handling missing values:\n")
print("Missing values in each column:\n")
print(df.isnull().sum()) # count of missing values in each column
df = df.dropna(subset=['CustomerID']) # drop rows with missing values
print(f"Dataset shape after dropping rows with missing CustomerID: {df.shape}")

#4.handle duplicates
print("Handling duplicates:\n")
duplicates = df.duplicated().sum()  # count of duplicate rows
print(f"Number of duplicate rows: {duplicates}")
df = df.drop_duplicates()   # drop duplicate rows
print(f"Dataset shape after dropping duplicates: {df.shape}")

#5.handle outliers
print("Handling outliers:\n")
print(f"min quantity before handling outliers: {df['Quantity'].min()}")
print(f"min unitprice before handling outliers: {df['UnitPrice'].min()}")

#num of rows with non-positive quantity
num_of_non_positive_quantity = df[(df['Quantity'] <= 0)].shape[0]
print(f"Number of rows with non-positive quantity: {num_of_non_positive_quantity}")

#num of rows with non-positive unit price
num_of_non_positive_unitprice = df[(df['UnitPrice'] <= 0)].shape[0]
print(f"Number of rows with non-positive unit price: {num_of_non_positive_unitprice}")

df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)] # filter out rows with non-positive values
print(f"Dataset shape after handling outliers: {df.shape}")

#6.data types and conversion
print("Data types and conversion:\n")

print("Data types before conversion:\n")
print(df[['InvoiceDate','CustomerID']].dtypes)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype(str)

print("Data types after conversion:\n")
print(df[['InvoiceDate','CustomerID']].dtypes)

#7.add new business fields

df['Sales'] = df['Quantity'] * df['UnitPrice']# add a new column 'Sales' which is the product of 'Quantity' and 'UnitPrice'

df['YearMonth'] = df['InvoiceDate'].dt.to_period('M') # add a new column 'YearMonth' which is the year and month of the invoice date

df['Weekday'] = df['InvoiceDate'].dt.dayofweek # add a new column 'Weekday' which is the day of the week of the invoice date

print("New columns added:\n")
print(df[['InvoiceDate','Quantity','UnitPrice','Sales','YearMonth','Weekday']].head(3))

#8.show the cleaned dataset info and summary statistics
print("Cleaned dataset information:\n")
print(f"Cleaned dataset shape: {df.shape}")
df.info()
print(df.head())

#9.save the cleaned dataset to a new csv file
df.to_csv('cleaned_ecommerce_data.csv', index=False)
print("Cleaned dataset saved to 'cleaned_ecommerce_data.csv'")