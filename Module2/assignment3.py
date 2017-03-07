import pandas as pd
import numpy as np

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df = pd.read_csv('C:/Users/IBM_ADMIN/Desktop/DATmaster/Module2/Datasets/servo.data', header = None)
df.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']
# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
new_df = df[df['vgain']==5]

print (len(new_df['vgain']))

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
neew = df[(df['motor'].str.contains('E')) &(df['screw'].str.contains('E'))]
print (len(neew))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
new_pgain = df[df['pgain'] == 4]
x= new_pgain.vgain.mean()
print (x)


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



