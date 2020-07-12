file_name = 'SalesJan2009.csv'
num_rows=0
for rows in open(file_name):
    num_rows+=1
print(num_rows)
