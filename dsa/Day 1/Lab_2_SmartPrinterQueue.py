""" 

"""

from collections import deque

urgent = deque()
normal = deque()

def add_job(job, priority):
    if priority.lower() == "urgent":
        urgent.append(job)
    else:
        normal.append(job)

def print_job():
    if urgent:
        print("Printing:", urgent.popleft())
    elif normal:
        print("Printing:", normal.popleft())
    else:
        print("No jobs to print")


add_job("Document1", "normal")
add_job("Report", "urgent")
add_job("Invoice", "normal")
add_job("Project", "urgent")

print_job()
print_job()
print_job()
print_job()
print_job()