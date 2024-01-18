def reduce(up, down):
    lst = up[:]
    for i in range(len(up)):
        lst[i] += max(down[i], down[i+1])
    return lst

T = int(input())
for case in range(T):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().strip().split(' '))))

    if n > 1:
        up = data[-2][:]
        down = data[-1][:]

        for i in range(n-2):
            down = reduce(up, down)
            up = data[-i-3][:]
        result = reduce(up, down)[0]
    else:
        result = data[0][0]
    print(result)


# Method 2
    
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s=[]
#     for _ in range(n):
#         s.append(list(map(int, input().split())))

#     row = n-2
#     while row>=0:
#         for i in range(len(s[row])):

#             s[row][i] += max(s[row+1][i], s[row+1][i+1])

#         row-=1
#     print(s[0][0])