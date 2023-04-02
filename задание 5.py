nums = input().split('  ')
b = {}
for num in nums:
    if num in b:
        b[num] += 1
    else:
        b[num] = 1
count = 0
for value in b.values():
    count += value * (value -1) // 2

print(count)