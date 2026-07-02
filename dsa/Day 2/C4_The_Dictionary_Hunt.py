""" 
c4) The Dictionary Hunt
You're in a library with a physical English dictionary. You need to find the word "Ephemeral". You don't start from page 1 — you open the middle, see "M", know E comes before M, so you take the left half and repeat.

"""



words = ["Apple", "Ball", "Cat", "Dog", "Ephemeral", "Fish", "Moon"]

target = "Ephemeral"

left = 0
right = len(words) - 1

while left <= right:
    mid = (left + right) // 2

    if words[mid] == target:
        print("Word found at position", mid)
        break
    elif words[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Word not found")