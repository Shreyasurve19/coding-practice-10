numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)