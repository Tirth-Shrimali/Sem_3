# Student Attendance using Array

attendance = ["Absent"] * 30

def markAttendance(rollNo):
    index = rollNo - 1
    attendance[index] = "Present"

# Mark attendance
markAttendance(5)
markAttendance(10)
markAttendance(16)
markAttendance(25)

# Display attendance
for i in range(30):
    print("Roll No.", i + 1, ":", attendance[i])