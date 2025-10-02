import sys

def last_fibonacci_digit(n: int) -> int:
    if n <= 1:
        return n
    fibonacci_series = [i for i in range(n+1)]
    fibonacci_series[0] = 0
    fibonacci_series[1] = 1
    for i in range(n+1):
        if i > 1:
            fibonacci_series[i] = (fibonacci_series[i-1] + fibonacci_series[i-2]) % 10
    return fibonacci_series[n]


def main():
    #n = int(input())
    
    fibonacci_sequence_sizes = sys.stdin.readline()
    input = list(map(int, fibonacci_sequence_sizes.split()))
    for n in input:
        print(last_fibonacci_digit(n))

if __name__ == "__main__":
    main()        

