import numpy as np
import pandas as pd
# Create an empty list to store the bills
bills = []

# Create a function to save a bill and extract its features
def save_bill(bill):
    # Extract the barcode, SKU code, product image and price from the bill
  barcode = bill.get_barcode()
  sku_code = bill.get_sku_code()
  product_image = bill.get_product_image()
  price = bill.get_price()
    # Create a dictionary with the bill data
  data = {'Bar Code': barcode, 'SKU Code': sku_code, 'Product Image' : product_image, 'Price': price}
    # Add the dictionary to the list of bills
  bills.append(data)

#Define Bill
class Bill:
    def __init__(self, barcode, sku_code, product_image, price):
        self.barcode = barcode
        self.sku_code = sku_code
        self.product_image = product_image
        self.price = price
    def get_barcode(self):
        return self.barcode
    def get_sku_code(self):
        return self.sku_code
    def get_product_image(self):
        return self.product_image
    def get_price(self):
        return self.price

# Save some bills
bill1 = Bill(barcode='12345', sku_code='A1', product_image='image1.jpg', price=100)
save_bill(bill1)

bill2 = Bill(barcode='23456', sku_code='A2', product_image='image2.jpg', price=200)
save_bill(bill2)

bill3 = Bill(barcode='34567', sku_code='B1', product_image='image3.jpg', price=150)
save_bill(bill3)

# Create a DataFrame from the list of bills
df = pd.DataFrame(bills)

# Print the DataFrame
print(df)