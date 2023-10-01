#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substringDiff' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s1
#  3. STRING s2
#

def diagonalSubstring(diagonal, first_diagonal_element, k, n, m, idx):
    diagonalLength = 0
    nextIdx = idx + 1
    lastIndex = diagonal.index(diagonal[-1])
    i = idx
    while k > 0 and i <= lastIndex:
      d_sub = diagonal[i]
      d_sub_length = d_sub[1]
      d_sub_distance = d_sub[2]
      diagonalLength += d_sub_length
      i += 1
      #if i >= lastIndex:
      #  nextIdx = lastIndex + 1
      if d_sub_distance <= k:
        diagonalLength += d_sub_distance
        k -= d_sub_distance
        if k== 0:
          d_sub = diagonal[i]
          d_sub_length = d_sub[1]
          diagonalLength += d_sub_length
  
      else:
        nextIdx = i + 1
        break
    
    fe_x = first_diagonal_element[0]
    fe_y = first_diagonal_element[1]
    if fe_x == 0 and fe_y == 0:
      if diagonalLength < min(n, m):
        diagonalLength += min(k, min(n, m) - diagonalLength)
    if fe_x != 0:
      if diagonalLength < min(n-fe_x+1, m):
        diagonalLength += min(k, min(n-fe_x+1, m) - diagonalLength)
    if fe_y != 0:
      if diagonalLength < min(m-fe_y+1, n):
        diagonalLength += min(k, min(m-fe_y+1, n) - diagonalLength)
    return diagonalLength
    

def substringDiff(k, s1, s2):
    # Write your code here
    n = len(s1)
    m = len(s2)
    max = 0

    # (n, m)
    substringsTable = [[0] * m for i in range(n)]

    # Each element of diagonal consists of:
    # key, denoting the first element of the diagonal
    # A value, containing a list of the substring in the diagonal:
    # The first element of the list is the initial position of the substring in the diagonal
    # The second element of the list is the length of the substring in the diagonal
    # The third element of the list is distance to the previous element of the diagonal, if exists 0 otherwise

    diagonals = {}

    # Base case
    for i in range(m):
      substringsTable[0][i] = int(s1[0] == s2[i])
      if substringsTable[0][i] > 0:
        diagonals[(0, i)] = []
        diagonals[(0, i)].append([(0, i), 1, float('inf')])
      if substringsTable[0][i] > max:
        max = substringsTable[0][i]

    for j in range(n):
      substringsTable[j][0] = int(s1[j] == s2[0])
      if substringsTable[j][0] > 0:
        diagonals[(j, 0)] = []
        diagonals[(j, 0)].append([(j, 0), 1, float('inf')])
      if substringsTable[j][0] > max:
        max = substringsTable[j][0]

    
    # General case
    for i in range(1, n):
      for j in range(1, m):
        substringsTable[i][j] =  (substringsTable[i-1][j-1] + 1) * int(s2[j] == s1[i])
        if substringsTable[i][j] > max:
          max = substringsTable[i][j]        
        if substringsTable[i][j] > 0:
          r = min(i, j)
          if (i - r, j - r) in diagonals:
            lastSubDiagonal = diagonals[(i - r, j - r)][-1]
            d_i = lastSubDiagonal[0][0]
            d_j = lastSubDiagonal[0][1]
            # If the current coordinates are to equal to he previous not zero element in the diagonal, it means we are dealing with a substrig and it is going to be treated as one single element
            if (i == (d_i + substringsTable[i][j] - 1)) and (j == (d_j + substringsTable[i][j] - 1)):
              lastSubDiagonal[1] += 1
            # Otherwise, the previous elemnt is a different substring
            else:
              # calculate the distance between the current substring and the previous one in the diagonal
              subLength = lastSubDiagonal[1]
              distance = (i - (d_i + subLength + 1) + 1)
              lastSubDiagonal[2] = distance
              diagonals[(i - r, j - r)].append([(i, j), 1, float('inf')])
          # empty diagonal; the new element is inserted in the dictionary
          else:
            diagonals[(i - r, j - r)] = []
            diagonals[(i - r, j - r)].append([(i, j), 1, float('inf')])


    for first_diagonal_element in diagonals:
      diagonal = diagonals[first_diagonal_element]
      idx = 0
      lastIndex = diagonal.index(diagonal[-1])
      length = diagonalSubstring(diagonal, first_diagonal_element, k, n, m, idx)
      if length > max:
        max = length
      while idx <= lastIndex:
        length = diagonalSubstring(diagonal, first_diagonal_element, k, n, m, idx)
        idx += 1
        if length > max:
          max = length

    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        k = int(first_multiple_input[0])

        s1 = first_multiple_input[1]

        s2 = first_multiple_input[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()