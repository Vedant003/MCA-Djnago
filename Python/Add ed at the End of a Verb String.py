verb = input("Enter a verb: ")
if verb.endswith("e"):
    result = verb + "d"
else:
    result = verb + "ed"

print(f"Resulting string: {result}")
