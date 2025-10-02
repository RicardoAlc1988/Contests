import sys

def gcd(a: int, b: int):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def lcm(a: int, b: int): 
    d = gcd(a, b)
    return int((a * b) / d)

def main():
    fibonacci_sequence_sizes = sys.stdin.readline()
    a, b  = list(map(int, fibonacci_sequence_sizes.split()))
    print(lcm(a, b))


if __name__ == "__main__":
    main()