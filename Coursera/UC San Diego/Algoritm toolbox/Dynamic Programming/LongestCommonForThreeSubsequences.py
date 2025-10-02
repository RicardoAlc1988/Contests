import sys



def longest_common_subsequence(n: int, seq1, m: int, seq2, l: int, seq3):
    
    maximum_subsequence = [
        [[0 for _ in range(l+1)] for _ in range(m+1)] for _ in range(n+1)]
    #print(seq1)
    #print(seq2)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l+1):
                max_solution = max(maximum_subsequence[i-1][j][k], 
                                   maximum_subsequence[i][j-1][k],
                                   maximum_subsequence[i][j][k-1],
                                   maximum_subsequence[i-1][j-1][k],
                                   maximum_subsequence[i-1][j][k-1],
                                   maximum_subsequence[i][j-1][k-1],
                                   maximum_subsequence[i-1][j-1][k-1] + int(
                                       seq1[i-1] == seq2[j-1]  == seq3[k-1]
                                       )
                                )
                #if seq1[i-1] == seq2[j-1]:
                #    max_solution = max(max_solution, maximum_subsequence[i-1][j-1] + 1)
                maximum_subsequence[i][j][k] = max_solution

    return maximum_subsequence[n][m][l]


def main():
    n = int(input())
    seq1_in = sys.stdin.readline()
    seq1 = list(map(int, seq1_in.split()))
    m = int(input())
    seq2_in = sys.stdin.readline()
    seq2 = list(map(int, seq2_in.split()))
    l = int(input())
    seq3_in = sys.stdin.readline()
    seq3 = list(map(int, seq3_in.split()))
    length_longest_common_subsequence = longest_common_subsequence(n, seq1, m, seq2, l, seq3)
    print(length_longest_common_subsequence)

if __name__ == "__main__":
    main()   
