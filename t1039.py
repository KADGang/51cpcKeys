n = int(input())
x = list(map(int, input().split()))
total = 0

for i in range(n):
    total = x[i] + total

print("{:.2f}".format(total / n))
