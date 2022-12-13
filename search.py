
A = [[("RB00001-GS1222", 1),("RB00002-GS1222", 1),("RB00003-GS1122", 1),("RC00004-GP0922", 0),("RC00005-GS0922", 1),("RE00006-SS1122", 1)],
          [("ES00010-YG1022", 1),("ES00012-YG0522", 1),("ED00007-GS0922", 0),("ED00009-WG1022", 1),("EJ00018-GS0622", 1),("EJ00020-GS1122", 0)],
          [("BC00022-YG1022", 0),("BC00015-YG0123", 1),("BC00014-GS0922", 1),("BC00008-RG1122", 1),("BO00028-GS0223", 1),("BF00027-YG1022", 1)],
          [("NP00030-GS0523", 1),("NP00032-GS0522", 1),("NC00031-DS0223", 0),("NC00036-GS0423", 1),("NC00037-DG0422", 1),("NC00039-GS0422",0)]]

k=input("Enter sku code:")

x=0
y=0
for l in A[0]:
    y=y+1
for l in A:
    x=x+1
r=-1
c=-1
# print(x,y)
for i in range(x):
    if(k[0]==A[i][0][0][0]):
        r=i
        break

if r>=0:
    for j in range(y):
        for o in range(1,14):
            if(k[o]==A[r][j][0][o]):
                if(o==13):
                    c=j
                    break
            else:
                break
            
if r>=0 and c>=0:
    print("Row Num is: ",r+1)
    print("Column Num is: ",c+1)
    print("Location is: (",r+1,",",c+1,")")
    if (A[r][c][1]==1):
        print("In Stock")
    else:
        print("Out of Stock")
else:
    print("Product NOT FOUND!!!")
