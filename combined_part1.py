import numpy as pd
import pandas as pd

# create a dictionary with the data for each example
data = {'Bar Code': ['A1B2C3', 'D4E5F6', 'G7H8I9', 'J0K1L2'],
        'SKU Code': ['MNOPQR', 'STUVWX', 'YZ1234', '567890'],
        'Product Image': ['product1.jpg', 'product2.jpg', 'product3.jpg', 'product4.jpg'],
        'Price': [12.99, 9.99, 19.99, 7.99]}

# create a DataFrame from the dictionary
original_df = pd.DataFrame(data)

# view the DataFrame
print(original_df)

#saving the DataFrame as a CSV File
original_df.to_csv('original_df.csv')

# Create an empty list to store the bills
bills = []

# Create a function to save a bill and extract its features
def save_bill(bill):
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

#saving the DataFrame as a CSV File
df.to_csv('df.csv')

# read in the datasets
Original_Dataset = pd.read_csv('original_df.csv')
Generated_Dataset = pd.read_csv('df.csv')

# create an empty list to store the results
results = []

# loop through the rows of the Generated_Dataset
for i, row in Generated_Dataset.iterrows():
    # get the SKU code from the current row
    sku = row['SKU Code']

    # check if the SKU code is in the Original_Dataset
    if sku in Original_Dataset['SKU Code'].values:
        # if it is, append 0 to the results list
        results.append(0)
    else:
        # if it's not, append 1 to the results list
        results.append(1)

# print the results
print(results)

# count the number of 1's in the list
num_ones = results.count(1)

# print the number of 1's
print(num_ones)