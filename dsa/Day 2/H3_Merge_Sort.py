""" 
h3) Merge Sort — The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists — one from its mobile app, one from railway counters. To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in one pass — compare the front of each list, pick the smaller token, advance. This is exactly merge sort's merge step.
"""



mobile = [2, 5, 8, 12]
counter = [1, 4, 9, 10]

merged = []

i = 0
j = 0

while i < len(mobile) and j < len(counter):
    if mobile[i] < counter[j]:
        merged.append(mobile[i])
        i += 1
    else:
        merged.append(counter[j])
        j += 1

while i < len(mobile):
    merged.append(mobile[i])
    i += 1

while j < len(counter):
    merged.append(counter[j])
    j += 1

print(merged)