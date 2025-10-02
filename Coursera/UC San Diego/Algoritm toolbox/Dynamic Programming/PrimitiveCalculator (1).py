import sys



def primitive_calculator(n: int):
    num_of_operations = [0] * n
    steps = [0] * n
    num_of_operations[0] = 0
    steps[0] = 0
    sol = []
    for i in range(1, n):
        #print(int((i + 1) / 2))
        #print(i, int((i + 1) / 2) - 1, num_of_operations[i-1] + 1, num_of_operations[int((i + 1) / 2) - 1], num_of_operations[int((i + 1) / 2) - 1] + 1 if (i + 1) % 2 == 0 else float('inf'), num_of_operations[int((i + 1) / 3) - 1] + 1 if (i + 1) % 3 == 0 else float('inf'))
        num_of_operations[i] = num_of_operations[i-1] + 1
        steps[i] = i - 1

        if (i + 1) % 2 == 0 and num_of_operations[int((i + 1) / 2) - 1] + 1 < num_of_operations[i]:
            num_of_operations[i] = num_of_operations[int((i + 1) / 2) - 1] + 1
            steps[i] = int((i + 1) / 2) - 1

        if (i + 1) % 3 == 0 and num_of_operations[int((i + 1) / 3) - 1] + 1 < num_of_operations[i]:
            num_of_operations[i] = num_of_operations[int((i + 1) / 3) - 1] + 1
            steps[i] = int((i + 1) / 3) - 1

    sol.append(n)
    index = n - 1
    while steps[index] > 0:
        sol.append(steps[index] + 1)
        index = steps[index]
    sol.append(1)
    return num_of_operations[n - 1], sol


def main():
    n = int(input())
    min_operations, sol = primitive_calculator(n)
    print(min_operations)
    # print(steps)
    #print(sol[::-1])
    print(" ".join(str(x) for x in reversed(sol)))

if __name__ == "__main__":
    main()   