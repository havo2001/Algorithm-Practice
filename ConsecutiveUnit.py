n = int(input())
max_length = 0
current_length = 0
y = 1000001
for i in range(n):
    x = int(input())
    if i == 0 or x != y:
        print(x)
    y = x
