#import pandas as pd
#import numpy as np

# Load data
#data = pd.read_csv('path/to/data')

# Example arrays
#Prices = [[300, 500], 2x2
          [1000, 120.85]]

#Array2 = [[200], [100]] 2x1 

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

# This is a way to return a vector from multi-dimensional array multiplication 
# This is one of 2 results of the matrix multiplication 
# If the Array2 is a simple array , it will be treated as a simple vector 

var = [200,100]
new_arr = []
# We start looping from the start of the price indices and initialise a row_sum variable which will reset to 0 every iteration
for i in range(len(Prices)):
    row_sum = 0
    #Since prices is a multidimensional list , they first element is also going to be a list and we are going to loop over the range of its size  
    for j in range(len(Prices[i])):  
        # So we multiply the prices row by the array2 column , since j only changes and i changes after j's iteration is done        
        row_sum += Prices[i][j] * var[j] 
        # We append the sum to the list as a normal result 
    new_arr.append(row_sum) 
print(new_arr)
