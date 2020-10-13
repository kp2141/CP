n, m = map(int, input().split())
matrix = [list(input()) for i in range(n)]
def rightfoo(matrix, i, j):

    try:
        if matrix[i][j + 1] == "a" and matrix[i][j + 2] == "b" and matrix[i][j + 3] == "a":
            return 1
        else:
            return 0
    except:
        return 0
def downfoo(matrix, i, j):

    try:
        if matrix[i + 1][j] == "a" and matrix[i + 2][j] == "b" and matrix[i + 3][j] == "a":
            return 1
        else:
            return 0
    except:
        return 0
def downrightfoo(matrix, i, j):

    try:
        if matrix[i + 1][j + 1] == "a" and matrix[i + 2][j + 2] == "b" and matrix[i + 3][j + 3] == "a":
            return 1
        else:
            return 0
    except:
        return 0
def uprightfoo(matrix, i, j):

    try:
        if i>=3 and matrix[i - 1][j + 1] == "a" and matrix[i - 2][j + 2] == "b" and matrix[i - 3][j + 3] == "a":
            return 1
        else:
            return 0
    except:
        return 0
ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "s":
            ans += rightfoo(matrix, i, j)
            ans += downfoo(matrix, i, j)
            ans += downrightfoo(matrix, i, j)
            ans += uprightfoo(matrix, i, j)

print(ans)