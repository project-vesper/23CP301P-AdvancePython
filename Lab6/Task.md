# Lab Assignment 6 : CSV In depth

You are working as a data engineer for a large retail company. Your team is responsible for
processing and analyzing sales data from multiple stores across the country. The sales data is
stored in CSV files, and each file represents sales data for a specific month and year. Each CSV
file has the following columns:

- Date (in the format "YYYY-MM-DD")
- Store ID (a unique alphanumeric code)
- Product ID (a unique alphanumeric code)
- Quantity sold (an integer representing the number of products sold on that date)

The "product_names.csv" file has two columns: "Product ID" and "Product Name," and it contains the mapping for all products in the sales data.

Your task is to write a Python program that performs the following operations:
- Read the sales data from all the CSV files in a given directory and its subdirectories.
- Calculate the total sales (quantity sold) for each product across all stores and all months.
- Determine the top 5 best-selling products in terms of the total quantity sold.
Create a new CSV file named "sales_summary.csv" and write the following information into it:
- Product ID
- Product Name
- Total Quantity Sold
- Average Quantity Sold per month (considering all months available in the data)