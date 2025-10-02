import sys

def huge_fibonacci_digit(n: int, m: int) -> int:
    if n <= 1:
        return n
    fib_mod_m = []
    fib_mod_m.append(0)
    fib_mod_m.append(1)
    is_sequence_completed = False
    sequence_index = 2
    while(not is_sequence_completed):
        next_fibonacci_element = (fib_mod_m[sequence_index-1] + fib_mod_m[sequence_index-2]) % m
        if next_fibonacci_element == 0 and (next_fibonacci_element + fib_mod_m[sequence_index-1]) % m == 1:
            is_sequence_completed = True 
        else:
            fib_mod_m.append(next_fibonacci_element)
            sequence_index = sequence_index + 1
    fib_sequence_length = len(fib_mod_m)
    #print(fib_mod_m)
    return fib_mod_m[n % fib_sequence_length]

def last_digit_fibonacci_sum(m: int, n: int):
    if m == 0:
        return (huge_fibonacci_digit(n+2, 10) - 1) % 10
    #print(huge_fibonacci_digit(n+2, 10))
    #print(huge_fibonacci_digit(m+1, 10))
    return (huge_fibonacci_digit(n+2, 10) - huge_fibonacci_digit(m+1, 10)) % 10


def main():
    #n = int(input())
    
    input = sys.stdin.readline()
    m, n = list(map(int, input.split()))
    print(last_digit_fibonacci_sum(m, n))

if __name__ == "__main__":
    main()