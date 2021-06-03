import pandas as pd
import time
# Returns true if there is a subset of set[] 
# with sun equal to given sum

data = pd.read_csv("test.csv")
data2 = data[["Money list"]]
data3 = data[["Amount to be withdrawn"]].values
set = data2.iloc[:,:].values

def isSubsetSum(set, n, sum):
    
    # The value of subset[i][j] will be 
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset =([[False for i in range(sum + 1)] 
            for i in range(n + 1)])
    # If sum is 0, then answer is true 
    for i in range(n + 1):
        subset[i][0] = True
    # If sum is not 0 and set is empty, 
    # then answer is false
    for i in range(1, sum + 1):
         subset[0][i]= False
             
    # Fill the subset table in botton up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<int(set[i-1]):
                subset[i][j] = subset[i-1][j]
            if j>= int(set[i-1]):
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])
    return subset[n][sum]

for i in range(len(set)):
    start_time = time.time()
    mang = set[i][0].split(",")
    mang[0] = mang[0].split("[")[1]
    mang[39] = mang[39].split("]")[0]
    sum = data3[i][0]
    for i in range(len(mang)):
        mang[i] = int(mang[i])
    n = len(mang)
    if (isSubsetSum(mang, n, sum) == True):
        print("Eligible Withdrawal Amount")
    else:
        print("Invalid Amount To Be Withdrawn")
    print(time.time()-start_time)
