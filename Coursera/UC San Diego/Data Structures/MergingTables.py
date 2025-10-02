import sys
import heapq
from collections import deque


class MergingTablesDUS:

    def __init__(self, length, values):
        self.values = values
        self.parent = [i for i in range(length)]
        self.rank = [0] * length
        self.max = max(values)


    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, destination, source):
        root_for_destination = self.find(destination)
        root_for_source = self.find(source)

        if root_for_source == root_for_destination:
            return
        
        if self.rank[root_for_destination] > self.rank[root_for_source]:
            self.parent[root_for_source] = root_for_destination
            self.values[root_for_destination] += self.values[root_for_source]
            self.values[root_for_source] = 0
            self.max = max(self.max, self.values[root_for_destination]) 

        else:
            self.parent[root_for_destination] = root_for_source
            self.values[root_for_source] += self.values[root_for_destination]
            self.values[root_for_destination] = 0
            self.max = max(self.max, self.values[root_for_source])             
            if self.rank[root_for_destination] == self.rank[root_for_source]:
                self.rank[root_for_source] = self.rank[root_for_source] + 1
               
        #self.max = max(self.max, self.values[self.find(destination)])
        #print(root_for_destination, root_for_source)
        #print(self.values)
        #print(self.parent)


    def get_max(self):
        return self.max

def merging_tables(n, tables_rows, queries):
    dus = MergingTablesDUS(n, tables_rows)
    for q in queries:
        destination, source = q
        dus.union(destination, source)
        print(dus.get_max())



def main():

    input_in = sys.stdin.readline()
    n, m = list(map(int, input_in.split()))
    tables_rows_in = sys.stdin.readline()
    tables_rows = list(map(int, tables_rows_in.split()))
    queries = []
    for _ in range(m):
        destination, source = map(int, input().split())
        queries.append((destination - 1, source - 1))
    merging_tables(n, tables_rows, queries)


if __name__ == "__main__":
    main()     