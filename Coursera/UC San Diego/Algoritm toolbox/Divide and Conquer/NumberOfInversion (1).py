import sys
import math
from itertools import accumulate
import random



def merge(A, B):
    #print(A, A_indices, B, B_indices)
    C = []
    i = j = 0
    num_of_inversions = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            num_of_inversions += (len(A) - i)
    C.extend(A[i:])
    C.extend(B[j:])
    return C, num_of_inversions

def merge_sort(n: int, elements):
    if n == 1:
        return elements, 0
    m = math.floor(n / 2)
    
    A, A_num_of_inversions = merge_sort(len(elements[:m]), elements[:m])
    
    B, B_num_of_inversions = merge_sort(len(elements[m:]), elements[m:])
    
    C, merge_num_of_inversion = merge(A, B)
    #print(f"A: {A}, B: {B}, C: {C}")
    # print(f"A: {A_num_of_inversions}, B: {B_num_of_inversions}, C: {merge_num_of_inversion}")
    num_of_inversions = A_num_of_inversions + B_num_of_inversions + merge_num_of_inversion

    return C, num_of_inversions


def main():
    n = int(input())
    elements_in = sys.stdin.readline()
    elements = list(map(int, elements_in.split()))
    _ , num_of_inversions = merge_sort(n, elements)
    print(num_of_inversions)

if __name__ == "__main__":
    main() 