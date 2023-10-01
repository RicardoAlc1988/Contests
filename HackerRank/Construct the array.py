import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    m = 10 ** 9 + 7
    
    c_arrays = [[0 for column in range(2)] for row in range(n)]
  
    # Base case
    c_arrays[0][0] = 1
    
    # General case
    for i in range(1, n):
      c_arrays[i][0] = ((k-1) * c_arrays[i-1][1]) % m
      c_arrays[i][1] = ((k-2) * c_arrays[i-1][1] + c_arrays[i-1][0]) % m
    if x == 1:
      return c_arrays[n-1][0] % m
    else:
      return c_arrays[n-1][1] % m
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()