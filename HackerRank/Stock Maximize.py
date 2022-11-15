#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    sol = [0] * len(prices)
    # this array contains the index k such that prices[i-k]...prices[i-1] is less or equal to prices[i] with k the largest , for each i
    less_than = [0] * len(prices)
    share_costs = [0] * len(prices)

    # general case
    for i in range(1, len(prices)):
        temp_less_than = i
        temp_share_cost = 0
        if prices[i] >= prices[i-1]:
            temp_less_than = i
            temp_share_cost = 0
            while temp_less_than > 0 and prices[temp_less_than-1] < prices[i]:
                if less_than[temp_less_than - 1] < temp_less_than - 1:
                    temp_share_cost = temp_share_cost + share_costs[temp_less_than-1] + prices[temp_less_than-1]
                    temp_less_than = less_than[temp_less_than - 1]
                else:
                    temp_share_cost = temp_share_cost + prices[temp_less_than-1]
                    temp_less_than = temp_less_than -1
        less_than[i] = temp_less_than
        share_costs[i] = temp_share_cost
        if temp_less_than > 0:
            sol[i] = max(-share_costs[i] + (i-temp_less_than) * prices[i] + sol[temp_less_than -1],  sol[i-1])
        else:
            sol[i] = max(-share_costs[i] + (i-temp_less_than) * prices[i],  sol[i-1])
    return sol[len(prices) - 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
