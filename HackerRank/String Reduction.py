#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringReduction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def calculate_irreductible(l_irreductible, vocab_element, red_operation):
    vocab_irreducible = []
    for sub_s in l_irreductible:
        n = len(sub_s)
        if len(sub_s) > 2:
            element = sub_s[0]
            if element == vocab_element:
                vocab_irreducible.append(sub_s + vocab_element)
            else:
                if n % 2 == 0:
                    vocab_irreducible.append(vocab_element)
                    vocab_irreducible.append(element + red_operation[frozenset([vocab_element, element])])
                else:
                    vocab_irreducible.append(red_operation[frozenset([vocab_element, element])])
                    vocab_irreducible.append(element + vocab_element)
        else:
            if n == 1:
                vocab_irreducible.append(sub_s + vocab_element)
                if sub_s[0] != vocab_element:
                    vocab_irreducible.append(red_operation[frozenset([sub_s[0], vocab_element])])
            elif n == 2:
                if sub_s[0] == sub_s[1]:
                    if sub_s[1] != vocab_element:
                        vocab_irreducible.append(vocab_element)
                        vocab_irreducible.append(sub_s[0] + red_operation[frozenset([sub_s[0], vocab_element])])
                    else:
                        vocab_irreducible.append(sub_s + vocab_element)
                else:
                    # Operations performed starting from sub_s[0] and sub_s[1]
                    red_01 = red_operation[frozenset([sub_s[0], sub_s[1]])]
                    vocab_irreducible.append(red_01 + vocab_element)
                    if red_01 != vocab_element:
                        vocab_irreducible.append(red_operation[frozenset([red_01, vocab_element])])

                    # Operations performed starting from sub_s[1] and vocab_element 
                    if sub_s[1] != vocab_element: 
                        red_0_elem = red_operation[frozenset([sub_s[1], vocab_element])]
                        vocab_irreducible.append(sub_s[0] + red_0_elem)
                        if sub_s[0] != red_0_elem:
                            vocab_irreducible.append(red_operation[frozenset([sub_s[0], red_0_elem])])
    return set(vocab_irreducible)

def stringReduction(s):
    # Write your code here
    red_operation = {frozenset(['a', 'b']): 'c',
                frozenset(['a', 'c']): 'b',
                frozenset(['b', 'c']): 'a'
                }

    n = len(s)
    vocab_size = 3
    a_ascii_int = ord('a')
    # size of matrix n + 1 x vocab_size
    #sol = [[ [] for i in range(vocab_size) ] for j in range(n + 1) ]
    sol = [ [] for i in range(n) ]

    # case base
    sol[0] = [s[0]]
  
    # general case
    for i in range(1, n):
        irreductible_set = calculate_irreductible(sol[i-1], s[i], red_operation)
        sol[i]  = list(irreductible_set)
    return min([len(x) for x in sol[n-1]])