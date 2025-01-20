
# Example arrays
Prices = [[300, 500], 
          [1000, 120.85]]

# method 1 (turning Array2 into a 2*1 array to be multiplied to the prices matrix)
Ans = []
Array2 = [[200], [100]]
for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[i])):    
        row_sum += Prices[i][j] * Array2[j][0]
    Ans.append(row_sum) 
print(Ans)


# method2

# (300*200 + 500*100) as an example calculation

# This is a way to return a vector from multi-dimensional array multiplication 
# This is one of 2 results of the matrix multiplication 
# If the Array2 is a simple array , it will be treated as a simple vector 

var = [200,100]
Ans2 = []
# We start looping from the start of the price indices and initialise a row_sum variable which will reset to 0 every iteration
for i in range(len(Prices)):
    row_sum = 0
    #Since prices is a multidimensional list , they first element is also going to be a list and we are going to loop over the range of its size  
    for j in range(len(Prices[i])):  
        # So we multiply the prices row by the array2 column , since j only changes and i changes after j's iteration is done        
        row_sum += Prices[i][j] * var[j] 
        # We append the sum to the list as a normal result 
    Ans2.append(row_sum) 
print(Ans2)
