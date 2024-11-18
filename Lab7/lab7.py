import csv
from fpdf import FPDF
from datetime import date
import os

def page(pdf,order_id,customer_name,product_name,quantity,unit_price,total_amount):
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, f"Invoice Number: {order_id}", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(169, 169, 169) #Gray background for headers
    pdf.cell(90, 10, "Field", 1, 0, "C", fill=True)
    pdf.cell(100, 10, "Value", 1, 1, "C", fill=True)

    #Set font for the table content
    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(245, 245, 245) #Light fill for rows

    pdf.cell(90, 10, "Date of Purchase:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, str(date.today()), 1, 1, "L")
    pdf.cell(90, 10, "Customer Name:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, customer_name, 1, 1, "L")
    pdf.cell(90, 10, "Product Name:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, product_name, 1, 1, "L")
    pdf.cell(90, 10, "Quantity:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, str(quantity), 1, 1, "L")
    pdf.cell(90, 10, "Unit Price:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, f"${unit_price:.2f}", 1, 1, "L")
    pdf.cell(90, 10, "Total Amount:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, f"${total_amount:.2f}", 1, 1, "L")

def process_csv(csv_file):
    order_ids = []
    pdf = FPDF()
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for order in reader:
            pdfIndividual=FPDF()
            order_id = order['OrderID']
            customer_name = order['CustomerName']
            product_name = order['ProductName']
            quantity = int(order['Quantity'])
            unit_price = float(order['UnitPrice'])
            total_amount = quantity * unit_price

            page(pdfIndividual,order_id,customer_name,product_name,quantity,unit_price,total_amount)
            page(pdf,order_id,customer_name,product_name,quantity,unit_price,total_amount)
            pdfIndividual.output(f"invoices/invoice_{order_id}.pdf")
            
    pdf.output("invoice.pdf")
    print("Invoice created!")

if __name__=="__main__":
    csv_file = input("Enter the CSV file name (e.g., orders.csv): ")
    
    if not os.path.exists('invoices/'):
        os.mkdir('invoices/')
    
    if not os.path.exists(csv_file):
        print(f"{csv_file} does not exist")
        exit()
    
    process_csv(csv_file)