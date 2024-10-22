def jobScheduling(jobs):
    # To sort all jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Identify maximum deadline .
    maxi = max(job[1] for job in jobs)

    # Initailly fill all slots with -1 upto deadline index
    slot = [-1] * (maxi + 1)

    # Arrangement of jobs with considering maximum deadline and identify the maximum profit and no. of jobs .
    countJobs = 0
    jobProfit = 0
    jobSequence = []

    for i in range(len(jobs)):
        for j in range(jobs[i][1], 0, -1):
            if slot[j] == -1:
                slot[j] = i
                countJobs += 1
                jobSequence.append(jobs[i][0])
                jobProfit += jobs[i][2]
                break

    return countJobs, jobProfit ,jobSequence
print("Name : Amol Subhash Dangat \nRoll No : 09 \n")
jobs = [(1, 4, 20), (2, 5, 60), (3, 6, 70), (4, 6, 65),(5, 4, 25), (6, 2,80), (7, 2, 10), (8, 2, 22)]
jobSequence = []
count, profit, jobSequence = jobScheduling(jobs)
print("Total Number of Jobs : ",count,"\nTotal Profit : ", profit, "\nJob Sequence : ",jobSequence)