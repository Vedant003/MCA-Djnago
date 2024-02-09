start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

sum_odd = sum(i for i in range(start_range, end_range + 1) if i % 2 != 0)
sum_even = sum(i for i in range(start_range, end_range + 1) if i % 2 == 0)

print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
