# import the necessary modules
import pandas as pd

# read in the datasets
Original_Dataset = pd.read_csv('Original_Dataset.csv')
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