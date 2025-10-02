import sys



def maximum_amount_of_gold(n: int, weights, W: int):
    
    max_amount_of_gold = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            best_solution = max_amount_of_gold[i-1][w]
            if w - weights[i-1] >= 0:
                best_solution = max(best_solution, max_amount_of_gold[i-1][w-weights[i-1]] + weights[i-1]) 
            
            max_amount_of_gold[i][w] = best_solution

    return max_amount_of_gold[n][W]


def main():
    input_in = sys.stdin.readline()
    W, n = list(map(int, input_in.split()))
    weigths_in = sys.stdin.readline()
    weigths = list(map(int, weigths_in.split()))
    max_amount_of_gold = maximum_amount_of_gold(n, weigths, W)
    print(max_amount_of_gold)

if __name__ == "__main__":
    main()