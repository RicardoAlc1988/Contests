import sys
from collections import deque

def simulate_processing_package(S: int, n: int, packet_times):
    processed_packages_times = []
    packages_queued = deque()
    current_time = 0    
    i = 0
    if packet_times and S > 0:
        packages_queued.append(packet_times[i])
        i = i + 1
    while packages_queued:
        # Retrieve the arrival time and processing time for the package currently being processed
        a_i, p_i = packages_queued[0]
        # Case for the packages which have been not inserted in the queue
        # print(a_i, p_i)
        if a_i == -1:
           processed_packages_times.append(-1)

        # Case for the packages whicih have been inserted in the queue
        else:
            # Calculate the time the ith-package stars
            start_time_for_ith_package = max(a_i, current_time)
            processed_packages_times.append(start_time_for_ith_package)
            # Update the queue based on the start time a_i and processing time p_i of the i-th package
            while i < n and packet_times[i][0] < start_time_for_ith_package + p_i:
                #print(i, packet_times, len(packages_queued), S)
                if len(packages_queued) < S:
                    packages_queued.append(packet_times[i])
                else:
                    packages_queued.append((-1, -1))
                i = i + 1
                
            # Update current_time after the ith-package has been processed
            current_time = start_time_for_ith_package + p_i
            # enqueue the next element, if exists
            if i < n:
                packages_queued.append(packet_times[i])
                i = i + 1
        packages_queued.popleft()
    return processed_packages_times

def main():
    input_in = sys.stdin.readline()
    S, n = list(map(int, input_in.split()))
    packet_times = []
    for _ in range(n):
        packet_time_i_in = sys.stdin.readline()
        arrived_time_for_ith_package, processed_time_for_ith_package = list(map(int, packet_time_i_in.split()))
        packet_times.append((arrived_time_for_ith_package, processed_time_for_ith_package))
    #print(packet_times)
    start_packages_times = simulate_processing_package(S, n, packet_times)
    for i in range(n):
        print(start_packages_times[i])


if __name__ == "__main__":
    main()