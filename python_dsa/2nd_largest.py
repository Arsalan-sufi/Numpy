arr = [2, 4, 1, 99]

first = second = -1

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)