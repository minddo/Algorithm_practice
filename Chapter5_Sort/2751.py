import sys
num = int(sys.stdin.readline())
items=[]
for i in range(num):
    item = int(sys.stdin.readline())
    items.append(item)
items.sort(reverse=False)
for item in items:
    print(item)

