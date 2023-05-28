class Job:
    def __init__(self, id, deadline, profit):##-------------->imp line
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduler():
    n = int(input("Enter the number of jobs: "))

    jobs = []
    max_deadline = 0

    for i in range(n):
        deadline, profit = map(int, input("Enter the deadline and profit of job {}: ".format(i + 1)).split()) ##----------------- imp line
        max_deadline = max(max_deadline, deadline)
        jobs.append(Job(i + 1, deadline, profit))

    jobs.sort(key=lambda x: x.profit, reverse=True) # job sort according to profit ##------------->imp line

    result = [0] * max_deadline
    slot = [False] * max_deadline

    max_profit = 0

    for i in range(n):
        deadline = jobs[i].deadline
        for j in range(deadline - 1, -1, -1):
            if not slot[j]:
                result[j] = jobs[i].id
                slot[j] = True+
                max_profit += jobs[i].profit
                break

    print("Max Profit Sequence of Jobs: ", end="")
    for i in range(max_deadline):
        if slot[i]:
            print(result[i], end=" ")

    print("\nMax Profit:", max_profit)

# Call the job scheduler
job_scheduler()
