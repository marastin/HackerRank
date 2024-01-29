# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_point_inside_triangle(x1, y1, x2, y2, x3, y3):
    # Calculate barycentric coordinates
    w1 = ((y2 - y3) * 0 + (x3 - x2) * 0 + x2 * y3 - x3 * y2) / ((y2 - y3) * x1 + (x3 - x2) * y1 + x2 * y3 - x3 * y2)
    w2 = ((y3 - y1) * 0 + (x1 - x3) * 0 + x3 * y1 - x1 * y3) / ((y3 - y1) * x2 + (x1 - x3) * y2 + x3 * y1 - x1 * y3)
    w3 = ((y1 - y2) * 0 + (x2 - x1) * 0 + x1 * y2 - x2 * y1) / ((y1 - y2) * x3 + (x2 - x1) * y3 + x1 * y2 - x2 * y1)

    # Check if (0, 0) is inside the triangle
    return 0 <= w1 <= 1 and 0 <= w2 <= 1 and 0 <= w3 <= 1


N = int(input())
result = 0
for _ in range(N):
    tri = list(map(int, input().split()))
    result += is_point_inside_triangle(*tri)
    
print(result)