belt = ["Phone", "Laptop", "Watch", "Mouse",
        "Keyboard", "Speaker", "Camera", "Printer"]

print("Product at Slot 3:", belt[3])

product = "Camera"
if product in belt:
    print(product, "found at Slot", belt.index(product))
else:
    print("Product not found")

belt[2] = "Tablet"
print("Updated Belt:", belt)

if None in belt:
    print("Belt is not full")
else:
    print("Belt is full")