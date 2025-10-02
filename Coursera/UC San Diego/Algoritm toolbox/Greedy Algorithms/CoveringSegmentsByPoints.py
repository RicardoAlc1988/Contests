import sys


def covering_segments_by_points(vertices):
    x_s = []
    ordered_vertices = sorted(vertices, key=lambda x: x[0], reverse=True)
    while ordered_vertices:
        last_vertex = ordered_vertices[0]
        x_i = last_vertex[0]
        x_s.append(x_i)
        vert_intersection = list(filter(lambda v: v[1] >= x_i, ordered_vertices))
        ordered_vertices = [v for v in ordered_vertices if v not in vert_intersection]

    return len(x_s), x_s


def main():
    vertices = []
    n = int(input())
    for _ in range(n):
        # lecture  of the segment

        segment_in = sys.stdin.readline()
        l_i, r_i = list(map(int, segment_in.split()))  
        vertices.append((l_i, r_i))
    
    n, x_s = covering_segments_by_points(vertices)
    print(n)
    print(*x_s)

if __name__ == "__main__":
    main()        

