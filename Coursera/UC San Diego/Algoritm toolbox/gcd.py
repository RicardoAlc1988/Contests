import sys

def gcd(a: int, b: int):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def main():
    fibonacci_sequence_sizes = sys.stdin.readline()
    a, b  = list(map(int, fibonacci_sequence_sizes.split()))
    print(gcd(a, b))


if __name__ == "__main__":
    main()