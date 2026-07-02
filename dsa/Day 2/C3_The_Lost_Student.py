""" 
c3) The Lost Student (Attendance Register)
Professor Sharma enters class and gets a call from the HOD — "Is Riya Desai present today?" The attendance register is not sorted. Names are written in the order students sat down.
"""



students = ["Aman", "Riya Desai", "Karan", "Neha", "Priya"]

name = "Riya Desai"

found = False

for i in range(len(students)):
    if students[i] == name:
        print(name, "is present at position", i + 1)
        found = True
        break

if not found:
    print(name, "is absent")