import sys
import math

def binary_search(n: int, elements, q):
    left = 0
    right = n-1
    while right >= left:
        m = math.floor( (left + right) / 2 )
        if elements[m] == q:
            return m
        elif elements[m] < q:
            left = m + 1
        else:
            right = m - 1
    return -1

def multiple_search(n: int, elements, q: int, queries):
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
    answers = multiple_search(n, elements, q, queries)
    print(*answers)

if __name__ == "__main__":
    main()        

