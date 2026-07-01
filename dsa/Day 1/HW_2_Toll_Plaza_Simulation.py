from collections import deque

queue = deque(maxlen=5)

queue.append("Car")
queue.append("Bus")
queue.append("Truck")
queue.append("Bike")
queue.append("Van")

print("Vehicles:", list(queue))

if len(queue) == 5:
    print("Queue is Full")

print("Passed:", queue.popleft())

queue.append("Auto")

print("Updated Queue:", list(queue))