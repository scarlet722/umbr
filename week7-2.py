numbers = [int(input()) % 42 for _ in range(10)]

unique_remainders = len(set(numbers))

print(unique_remainders)
