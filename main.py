n = int(input())
a = list(map(int, input().split()))

items = []
for i in range(n):
    items.append((a[i], i))

items.sort()

left = 0
right = n - 1

answer = []

for _ in range(n - 1):
    if items[left][1] < items[right][1]:
        answer.append(items[right][0])
        right -= 1
    else:
        answer.append(items[left][0])
        left += 1

print(' '.join(map(str, answer)))