
import sys



def splitting_pirate_loot(i: int, sum_set_1: int, sum_set_2 : int, sum_set_3: int, loot, result_cache):
    
    if (i, sum_set_1, sum_set_2, sum_set_3) in result_cache:
        return result_cache[(i, sum_set_1, sum_set_2, sum_set_3)]
    
    if i == 0:
        if sum_set_1 == 0 and sum_set_2 == 0 and sum_set_3 == 0:
            return 1
        else:
            return 0
    best_result = max(splitting_pirate_loot(i-1, sum_set_1 - loot[i-1], sum_set_2, sum_set_3, loot, result_cache),
                      splitting_pirate_loot(i-1, sum_set_1, sum_set_2 - loot[i-1], sum_set_3, loot, result_cache),
                      splitting_pirate_loot(i-1, sum_set_1, sum_set_2, sum_set_3 - loot[i-1], loot, result_cache)
                     )
    result_cache[(i, sum_set_1, sum_set_2, sum_set_3)] = best_result
    return best_result

def exists_loot_split(n: int, loot):
    total_loot = sum(loot)
    quotient, remainder = divmod(total_loot, 3)
    if remainder != 0:
        return 0
    return splitting_pirate_loot(n, quotient, quotient, quotient, loot, {})


def main():
    n = int(input())
    loot_in = sys.stdin.readline()
    loot = list(map(int, loot_in.split()))
    loot_split_solution = exists_loot_split(n, loot)
    print(loot_split_solution)

if __name__ == "__main__":
    main()