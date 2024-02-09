number = int(input("Enter a number: "))
num_str = str(number)
order = len(num_str)

sum_digits = sum(int(digit) ** order for digit in num_str)

if sum_digits == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
