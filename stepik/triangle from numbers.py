n = int(input())
counter = 1

for row in range(1, n+1):
    for j in range(1, row+1):
        print(counter, end=' ')
        counter += 1
    print()

