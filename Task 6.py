x1 = int(input("Enter x1 = " ))
x2 = int(input("Enter x2 = "))
y1 = int(input("Enter y1 = "))
y2 = int(input("Enter y2 = "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')