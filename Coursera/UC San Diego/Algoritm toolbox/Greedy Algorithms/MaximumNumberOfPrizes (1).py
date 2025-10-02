import sys
import math


def maximum_number_of_prices(n: int):
    addends = []
    sum = 0
    best_solution = 0
    # m is the most approximate integer such that the sum of the m first positive integers is the most closest to n
    m = math.floor( (-3 + math.sqrt(9 + 8 * (n-1) ) ) / 2 )
    for i in range(m):
        addends.append(i+1)
        sum = sum + (i+1)
    addends.append(n - sum)
    best_solution = m + 1
    return best_solution, addends


def main():
    n = int(input())
    
    best_solution, addends = maximum_number_of_prices(n)
    print(best_solution)
    print(*addends)

if __name__ == "__main__":
    main()        

