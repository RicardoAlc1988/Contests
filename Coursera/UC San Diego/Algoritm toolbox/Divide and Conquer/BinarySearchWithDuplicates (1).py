import sys
import math


def binary_search(n: int, elements, q):
    left = 0
    right = n-1
    while right > left:
        m = math.floor( (left + right) / 2 )
        if elements[m] == q:
            right = m
        elif elements[m] <= q:
            left = m + 1
        else:
            right = m - 1
        #print(left, right, m, elements[m])
    if elements[left] == q:
        return left
    return -1


def binary_search_wtih_duplicates(n: int, elements, q: int, queries):
    queries_answers = []
    for q in queries:
        answer_to_q = binary_search(n, elements, q)
        queries_answers.append(answer_to_q)
    return queries_answers


def main():
    n = int(input())
    elements_in = sys.stdin.readline()
    elements = list(map(int, elements_in.split()))
    q = int(input())
    queries_in = sys.stdin.readline()
    queries = list(map(int, queries_in.split()))
    #answer = binary_search(n, elements, 2)
    answers = binary_search_wtih_duplicates(n, elements, q, queries)
    print(*answers)

if __name__ == "__main__":
    main()   