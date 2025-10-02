import sys

def fibonacci_number(n: int):
    if n <= 1:
        return n
    fib_sequence = [0] * (n+1)
    fib_sequence[0] = 0
    fib_sequence[1] = 1
    for i in range(2, n+1):
        #print(i)
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    return fib_sequence[n]

def main():
    fibonacci_sequence_sizes = sys.stdin.readline()
    input = list(map(int, fibonacci_sequence_sizes.split()))
    for n in input:
        print(fibonacci_number(n))


if __name__ == "__main__":
    main()

