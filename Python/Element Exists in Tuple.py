my_tuple = (1, 2, 3, 4, 5)
element_to_check = int(input("Enter an element to check: "))

if element_to_check in my_tuple:
    print(f"{element_to_check} exists in the tuple")
else:
    print(f"{element_to_check} does not exist in the tuple")
