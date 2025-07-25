from fcfs import fcfs_scheduling

def main():
    num_processes = int(input("Enter number of processes: "))

    arrival_times = []
    burst_times = []

    for i in range(num_processes):
        arrival = int(input(f"Enter Arrival Time for P{i+1}: "))
        burst = int(input(f"Enter Burst Time for P{i+1}: "))
        arrival_times.append(arrival)
        burst_times.append(burst)

    fcfs_scheduling(arrival_times, burst_times)

if __name__ == "__main__":
    main()
