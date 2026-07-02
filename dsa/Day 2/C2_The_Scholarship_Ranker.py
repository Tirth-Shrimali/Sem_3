""" 
C2) The Scholarship Ranker
A college must give scholarships to the top 3 scorers. The coordinator scans the entire marksheet, finds the highest scorer, moves them to position 1. Then scans the remaining students for the next highest, and so on. Each pass = one full scan to select the minimum/maximum.
"""



marks = [78, 95, 62, 88, 91]

n = len(marks)

for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if marks[j] > marks[max_index]:
            max_index = j
    marks[i], marks[max_index] = marks[max_index], marks[i]

print("Top 3 Scorers:", marks[:3])