def fcfs_scheduling(arrival_times, burst_times):
    n = len(burst_times)
    processes = list(range(n))

    # Sort processes by arrival time
    processes.sort(key=lambda x: arrival_times[x])

    waiting_time = [0] * n
    turnaround_time = [0] * n
    start_time = [0] * n

    current_time = 0

    for i in processes:
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        start_time[i] = current_time
        waiting_time[i] = current_time - arrival_times[i]
        current_time += burst_times[i]
        turnaround_time[i] = waiting_time[i] + burst_times[i]

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Printing results
    print("\nScheduling Results:")
    print("Process\tArrival\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"P{i+1}\t{arrival_times[i]}\t{burst_times[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    # Gantt Chart
    print("\n🕒 Gantt Chart:")
    print("|", end="")
    for i in processes:
        print(f" P{i+1} |", end="")
    print()

    # Print timeline below Gantt chart
    print(start_time[processes[0]], end="\t")
    for i in processes:
        end_time = start_time[i] + burst_times[i]
        print(end_time, end="\t")
    print()
