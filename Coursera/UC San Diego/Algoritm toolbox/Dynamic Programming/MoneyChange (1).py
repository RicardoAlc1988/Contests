import sys



def money_change(n: int):
    num_of_coins = [0] * (n + 1)
    for i in range(1, n + 1):
        num_of_coins[i] = min(num_of_coins[i - 1] + 1,
                              num_of_coins[i - 3] + 1 if (i - 3) >= 0 else float('inf'),
                              num_of_coins[i - 4] + 1 if (i - 4) >= 0 else float('inf'),
                             )

    return num_of_coins[n]


def main():
    n = int(input())
    min_number_of_coins = money_change(n)
    print(min_number_of_coins)

if __name__ == "__main__":
    main()   