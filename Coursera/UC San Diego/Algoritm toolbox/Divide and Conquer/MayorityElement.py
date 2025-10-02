import sys
import math

def merge(A, B):
    C = []
    while A and B:
        a = A[0]
        b = B[0]
        if a[0] == b[0]:
            C.append( (a[0], a[1] + b[1]) )
            A.pop(0)
            B.pop(0)
        elif a[0] < b[0]:
            C.append( (a[0], a[1]) )
            A.pop(0)
        else:
            C.append( (b[0], b[1]) )
            B.pop(0)
    while A:
        a = A.pop(0)
        C.append( (a[0], a[1]) )                        
    while B:
        b = B.pop(0)
        C.append( (b[0], b[1]) )
    return C

def merge_sort_modified(n: int, elements):
    if n == 1:
        return [(elements[0], 1)]
    m = math.floor(n / 2)
    A = merge_sort_modified(len(elements[:m]), elements[:m])
    B = merge_sort_modified(len(elements[m:]), elements[m:])
    C = merge(A, B)
    return C

def mayority_element(n: int, elements):
    elements_by_occurence = merge_sort_modified(n, elements)
    max_element = (-1, 0)
    for i in range(len(elements_by_occurence)):
        if elements_by_occurence[i][1] > max_element[1]:
            max_element = elements_by_occurence[i]
    return (int)(max_element[1] > math.floor(n / 2))


def main():
    n = int(input())
    elements_in = sys.stdin.readline()
    elements = list(map(int, elements_in.split()))
    exists_mayority_element = mayority_element(n, elements)
    print(exists_mayority_element)

if __name__ == "__main__":
    main()        

