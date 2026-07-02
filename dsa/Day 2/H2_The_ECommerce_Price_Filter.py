""" 
h2) The E-Commerce Price Filter (First occurrence ≥ target)
You're on Flipkart. You filter products: "Show me laptops priced ₹50,000 or above." Products are sorted by price. Flipkart must find the first product ≥ ₹50,000 — classic binary search variant called lower bound.
"""



prices = [32000, 41000, 47000, 52000, 58000, 65000]

target = 50000

left = 0
right = len(prices) - 1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if prices[mid] >= target:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

if answer != -1:
    print("First laptop price:", prices[answer])
else:
    print("No laptop found")