import csv
import os
from collections import defaultdict

def readData():
    products={}
    if (os.path.exists('product_names.csv')):
        with open('product_names.csv','r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                products[row['Product ID']]=row['Product Name']
    
    sales_data=[]
    for file in os.listdir():
        if file.endswith('.csv') and file!='product_names.csv' and file!='sales_summary.csv':
            with open(file,'r') as f:
                reader=csv.DictReader(f)
                data=[row for row in reader]
                sales_data.extend(data)
    
    return products,sales_data

def salesSummary(data):
    sales = defaultdict(int)
    months = set()

    for row in data:
        product_id = row['Product ID']
        quantity_sold = int(row['Quantity sold'])
        date = row['Date']
        year_month = date[:7]

        sales[product_id] += quantity_sold
        months.add(year_month)
    
    return sales, len(months)

def writeSummary(sales,products,filename,months):
    summary_data=[]

    for productID,productName in products.items():
        totalSales=sales.get(productID,0)
        average = totalSales/months if months>0 else 0

        summary_data.append({
            'productID':productID,
            'productName':productName,
            'totalSales':totalSales,
            'averageSales':average
        })
    
    with open(filename,'w') as file:
        writer=csv.DictWriter(file,['productID','productName','totalSales','averageSales'])
        writer.writeheader()
        for product in summary_data:
            writer.writerow(product)

if __name__=="__main__":
    products,sales_data=readData()
    sales,months=salesSummary(sales_data)
    writeSummary(sales,products,'sales_summary.csv',months)
