import sys



def longest_common_subsequence(n: int, seq1, m: int, seq2):
    
    maximum_subsequence = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    #print(seq1)
    #print(seq2)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            max_solution = max(maximum_subsequence[i][j-1], 
                               maximum_subsequence[i-1][j], 
                               maximum_subsequence[i-1][j-1] + int(seq1[i-1] == seq2[j-1])
                               )
            #if seq1[i-1] == seq2[j-1]:
            #    max_solution = max(max_solution, maximum_subsequence[i-1][j-1] + 1)
            maximum_subsequence[i][j] = max_solution

    return maximum_subsequence[n][m]


def main():
    n = int(input())
    seq1_in = sys.stdin.readline()
    seq1 = list(map(int, seq1_in.split()))
    m = int(input())
    seq2_in = sys.stdin.readline()
    seq2 = list(map(int, seq2_in.split()))
    length_longest_common_subsequence = longest_common_subsequence(n, seq1, m, seq2)
    print(length_longest_common_subsequence)

if __name__ == "__main__":
    main()   