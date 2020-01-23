x = int(input())
y = []
y = list(map(int, input().split()))
total = 0

for i in range(len(y)):
    total = total + y[i]

print(total)
