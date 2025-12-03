even_numbers: list[int] = []
for i in range(1, 100):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)