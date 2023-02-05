n = int(input())
l = list(map(int, input().split(" ")))

maximum = l[0]
ans = 0
for i in range(n):
    maximum = max(l[i], maximum)
    if l[i] < maximum:
        ans = -1
        break

if ans == 0:
    print(max(l) - min(l))
else:
    print(ans)
