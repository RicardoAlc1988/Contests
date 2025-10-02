import sys


def car_fueling(d: int, m: int, stops) -> int:
    pos_actual = 0
    num_of_stops = 0
    while pos_actual + m < d:
        posible_stops = [x for x in stops if  x > pos_actual and x <= m + pos_actual]
        if not posible_stops:
            return -1
        selected_stop = max(posible_stops)
        pos_actual = selected_stop
        #stops = [v for v in stops if v not in posible_stops]
        num_of_stops = num_of_stops + 1
    return num_of_stops


def main():
    d = int(input())
    m = int(input())
    n = int(input())
    stops_in = sys.stdin.readline()
    stops = list(map(int, stops_in.split()))
    num_of_stops = car_fueling(d, m, stops)
    print(num_of_stops)

if __name__ == "__main__":
    main()        

