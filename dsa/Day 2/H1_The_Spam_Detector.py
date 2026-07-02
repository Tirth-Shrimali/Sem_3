""" 
h1) - The Spam Detector (Search in Stream) – linear search
A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against a blacklist of known spam sender IDs. The blacklist has no order.
"""



blacklist = [1023, 2056, 4089, 5500, 7821]

sender = 4089

if sender in blacklist:
    print("Spam sender detected")
else:
    print("Safe sender")