import numpy as np
import pandas as pd

A = [[("RB00001-GS1222", 1),("RB00002-GS1222", 1),("RB00003-GS1122", 1),("RC00004-GP0922", 0),("RC00005-GS0922", 1),("RE00006-SS1122", 1)],
          [("ES00010-YG1022", 1),("ES00012-YG0522", 1),("ED00007-GS0922", 0),("ED00009-WG1022", 1),("EJ00018-GS0622", 1),("EJ00020-GS1122", 0)],
          [("BC00022-YG1022", 0),("BC00015-YG0123", 1),("BC00014-GS0922", 1),("BC00008-RG1122", 1),("BO00028-GS0223", 1),("BF00027-YG1022", 1)],
          [("NP00030-GS0523", 1),("NP00032-GS0522", 1),("NC00031-DS0223", 0),("NC00036-GS0423", 1),("NC00037-DG0422", 1),("NC00039-GS0422",0)]]


print(A)

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
bill1 = Bill(barcode='12345', sku_code='RB00001-GS1222', product_image='image1.jpg', price=14230)
save_bill(bill1)

bill2 = Bill(barcode='23456', sku_code='EJ00018-GS0622', product_image='image2.jpg', price=27070)
save_bill(bill2)

bill3 = Bill(barcode='34567', sku_code='NC00036-GS0423', product_image='image3.jpg', price=40800)
save_bill(bill3)

# print(bills)
# Create a DataFrame from the list of bills
df = pd.DataFrame(bills)

codes = df.loc[:,"SKU Code"]
print(codes)

numberBills = len(bills)
i = 0
while i<numberBills:
  k = codes[i]

  x=0
  y=0
  for l in A[0]:
      y=y+1
  for l in A:
      x=x+1
  r=-1
  c=-1
  # print(x,y)
  for m in range(x):
    for n in range(y):
      if(k==A[m][n][0]):
          A[m][n] = (k,0)
  
  i = i+1

print(A)

count = 0
for m in range(x):
    for n in range(y):
      if(A[m][n][1] == 1):
        count = count + 1
      else:
        continue

# stock count
print(count)
