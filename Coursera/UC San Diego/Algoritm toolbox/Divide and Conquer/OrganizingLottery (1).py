import sys
import math
from itertools import accumulate
import random

def merge(A, A_indices, B, B_indices):
    #print(A, A_indices, B, B_indices)
    C = []
    C_indices = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            C_indices.append(A_indices[i])
            i += 1
        else:
            C.append(B[j])
            C_indices.append(B_indices[j])
            j += 1
    C.extend(A[i:])
    C_indices.extend(A_indices[i:])
    C.extend(B[j:])
    C_indices.extend(B_indices[j:])
    return C, C_indices

def merge_sort(n: int, elements, indices):
    if n == 1:
        return elements, indices
    m = math.floor(n / 2)
    A, A_indices = merge_sort(len(elements[:m]), elements[:m], indices[:m])
    #print(f"A: {A}; indices: {A_indices}")
    B, B_indices = merge_sort(len(elements[m:]), elements[m:], indices[m:])
    #print(f"B: {B}; indices: {B_indices}")
    C, C_indices = merge(A, A_indices, B, B_indices)
    #print(f"C: {C}; indices: {C_indices}")
    return C, C_indices 

def bisection_modified_upper_bound(n: int, elements, upper: int):
    if elements[0] >  upper:
        return -1
    if upper >= elements[-1]:
        return n-1
    max_index_lt_upper = 0
    search_space = elements
    while len(search_space) > 1:
        m = math.floor( len(search_space) / 2 )
        if search_space[m] > upper:
           search_space = search_space[:m]
           #if len(search_space) == 1 and search_space[0] <= upper:
           #    max_index_lt_upper += 1
        else:
            search_space = search_space[m:]
            max_index_lt_upper += m
    return max_index_lt_upper    

def organizing_lottery(m: int, n: int, segments, points):
    # order the points
    indices = [i for i in range(n)]
    points_ordered, indices_ordered = merge_sort(n, points, indices)
    # order the segments using its natural order
    segments_ordered, _ = merge_sort(m, segments, indices)
    i = j = 0
    diff_array = [0] * (n + 1)
    while j < m and i < n:
        # Find the first point greater or equal than the first element of the current segment
        while i < (n - 1) and points_ordered[i] < segments_ordered[j][0]:
            i += 1
        #print(f"i: {i}; j: {j} {segments_ordered[j]}")
        if segments_ordered[j][0] <= points_ordered[i] and segments_ordered[j][1] >= points_ordered[i]:
            # Calculate how many points are intersected by the current segmnet, by using bisection method
            last_index_lt_segment_y = bisection_modified_upper_bound(n, points_ordered, segments_ordered[j][1])
            #print(f"Segmento con coordenadas x: {segments_ordered[j][0] }, {segments_ordered[j][1]} interseca al rango de puntos {points_ordered[i]} , {points_ordered[last_index_lt_segment_y]}, with index {last_index_lt_segment_y}")
            diff_array[i] += 1
            if last_index_lt_segment_y + 1 < n:
                diff_array[last_index_lt_segment_y + 1] -= 1
        j += 1
        # point_max = bisection_modified_upper_bound(n: int, elements, upper: int)
    #print(f"indices ordered: {indices_ordered}")
    #print(f"diff array : {diff_array}")
    num_segments = list(accumulate(diff_array))[:-1]
    #print(f"num segments : {num_segments}")
    sol = [0]  * n
    for i in range(n):
        sol[indices_ordered[i]] = num_segments[i]
    #num_segments_by_point = [num_segments[indices_ordered[i]] for i in range(n)]
    return sol



########################################## STRESS TEST ##########################################

def organizing_lottery_naive(m: int, n: int, segments, points):
    sol = [0] * n 
    for i in range(n):
        for j in range(m):
            if segments[j][0] <= points[i] and points[i] <= segments[j][1]:
                sol[i] += 1
    return sol


def stress_test():
    points = []
    segments = []
    inf = -100
    sup = 100
    m = random.randint(1, 15)
    n = random.randint(1, 15)
    while True:
        for _ in range(n):
            points.append(random.randint(inf, sup))

        for _ in range(m):
            seg_x = random.randint(inf, sup)
            seg_y = random.randint(seg_x, sup)
            segments.append((seg_x, seg_y))

        print(m, n)
        for j in range(m):
            print(segments[j])
        print(points)
        
        sol_1 = organizing_lottery_naive(m, n, segments, points)
        print(f"naive solution: {sol_1}")
        sol_2 = organizing_lottery(m, n, segments, points)
        print(f"O(nlog(n)) solution: {sol_2}")
        if sol_1 != sol_2:
            print(f"naive solution: {sol_1}")
            print(f"O(nlog(n)) solution: {sol_2}")
            return



def main():

    #stress_test()

    #points_in = sys.stdin.readline()
    #points = list(map(int, points_in.split()))
    #index =  bisection_modified_upper_bound(len(points), points, 5)
    #print(index)

    input_size = sys.stdin.readline()
    m, n = map(int, input_size.split())
    segments = []
    for _ in range(m):
        segment_in = sys.stdin.readline()
        segmnet_x, segment_y = map(int, segment_in.split())
        segments.append((segmnet_x, segment_y))
    points_in = sys.stdin.readline()
    points = list(map(int, points_in.split()))

    #indices = [i for i in range(len(points))]
    #merge_sort(len(points), points, indices)
    num_segments_by_point = organizing_lottery(m, n, segments, points)
    print(*num_segments_by_point)

    #indices = [i for i in range(n)]
    #a, b = merge_sort(n, points, indices)
    #print(a, b)
    #num_segments_by_point = organizing_lottery(m, n, segments, points)

    #num_segments_by_point = organizing_lottery_naive(m, n, segments, points)
    #print(*num_segments_by_point)

if __name__ == "__main__":
    main()        

