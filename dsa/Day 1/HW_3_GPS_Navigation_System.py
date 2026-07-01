backStack = []
forwardStack = []
current = "Home"

def visit(place):
    global current
    backStack.append(current)
    current = place
    forwardStack.clear()

def back():
    global current
    if backStack:
        forwardStack.append(current)
        current = backStack.pop()

def forward():
    global current
    if forwardStack:
        backStack.append(current)
        current = forwardStack.pop()

visit("Park")
visit("Mall")
visit("Station")

print("Current:", current)

back()
print("After Back:", current)

back()
print("After Back:", current)

forward()
print("After Forward:", current)