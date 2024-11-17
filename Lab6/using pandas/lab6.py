import os
import pandas as pd

def read_sales_data():
    sales_data = []

    for file in os.listdir():
        if file.endswith('.csv') and 'product_names.csv' not in file and 'sales_summary.csv' not in file :
            sales_data.append(pd.read_csv(file))

    all_sales_data = pd.concat(sales_data, ignore_index=True)
    return all_sales_data

def calculate_sales_summary(sales_data, product_names):
    total_sales = sales_data.groupby('Product ID')['Quantity sold'].sum().reset_index()
    sales_summary = pd.merge(total_sales, product_names, on='Product ID')
    return sales_summary

def save_top_selling_products(sales_summary, top_n=5):
    top_selling_products = sales_summary.head(top_n)
    top_selling_products.to_csv('sales_summary.csv', index=False)

if __name__ == "__main__":
    product_names = pd.read_csv('product_names.csv')
    sales_data = read_sales_data()
    sales_summary = calculate_sales_summary(sales_data, product_names)
    save_top_selling_products(sales_summary)