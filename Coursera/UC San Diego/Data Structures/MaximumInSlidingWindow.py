import sys
from collections import deque


def maximum_in_sliding_window(n: int, sequence, m: int):
    # stack initialization
    maximum_in_window = []
    stack = deque()

    # index initialization
    window_pointer = 1
    index_pointer = m - 1
    while index_pointer < n:
        maximum_value_out_of_window = -1
        #stack initialization
        for i in range(m):
            prev_element = None
            if stack:
                prev_element = stack[0]
            #print(stack, prev_element, sequence[m-i-1])
            next_element = max(sequence[window_pointer * m-i-1], prev_element if prev_element is not None else -1)
            stack.appendleft(next_element)
        #print(stack)
        while stack and index_pointer < n:
            if sequence[index_pointer] > maximum_value_out_of_window:
                maximum_value_out_of_window = sequence[index_pointer]
            element = stack.popleft()
            #print(index_pointer, maximum_value_out_of_window, stack, maximum_in_window, element)
            max_window = max(maximum_value_out_of_window, element)
            maximum_in_window.append(max_window)
            index_pointer = index_pointer + 1
        window_pointer = window_pointer + 1
    return maximum_in_window

def main():
    n = int(input())
    sequence_in = sys.stdin.readline()
    sequence = list(map(int, sequence_in.split()))
    m = int(input())
    maximum_in_window = maximum_in_sliding_window(n, sequence, m)
    print(*maximum_in_window)

if __name__ == "__main__":
    main()   