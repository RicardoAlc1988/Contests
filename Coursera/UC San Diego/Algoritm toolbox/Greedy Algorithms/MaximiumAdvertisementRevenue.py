import sys


def maxumum_advertisement_revenue(n: int, prices, clicks):
    max_revenue = 0
    ordered_prices = sorted(prices, reverse=True)
    ordered_clicks = sorted(clicks, reverse=True)
    for i in range(n):
        max_revenue = max_revenue + ordered_prices[i] * ordered_clicks[i]

    return max_revenue


def main():
    n = int(input())
    prices_in = sys.stdin.readline()
    prices = list(map(int, prices_in.split()))
    clicks_in = sys.stdin.readline()
    clicks = list(map(int, clicks_in.split()))
    max_revenue = maxumum_advertisement_revenue(n, prices, clicks)
    print(max_revenue)

if __name__ == "__main__":
    main()        

