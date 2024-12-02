import random

def print_matrix(matrix, name):
    print(f"Matrix {name}:")
    for row in matrix:
        print(' '.join(map(str, row)))

def count_pos_even_region2(matrix):
    n = len(matrix)
    count = 0
    for i in range(n // 2):
        for j in range(n // 2, n):
            if matrix[i][j] > 0 and j % 2 == 1:
                count += 1
    return count

def count_neg_odd_region4(matrix):
    n = len(matrix)
    count = 0
    for i in range(n // 2, n):
        for j in range(n // 2):
            if matrix[i][j] < 0 and j % 2 == 0:
                count += 1
    return count

def swap_regions3_4(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n // 2, n):
            matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]

def swap_regions2_3(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j], matrix[i][j + n // 2] = matrix[i][j + n // 2], 0 # Несимметричный обмен: 2 -> 3, 3 -> 0


n = int(input("Введите размер матрицы (от 3 и больше, нечетное число): "))
while n < 3 or n % 2 == 0:
    n = int(input("Некорректный ввод. Введите нечетное число от 3 и больше: "))

K = int(input("Введите число K: "))

A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
F = [row[:] for row in A]

print_matrix(A, "A")

pos_even_2 = count_pos_even_region2(F)
neg_odd_4 = count_neg_odd_region4(F)

if pos_even_2 > neg_odd_4:
    swap_regions3_4(F)
else:
    swap_regions2_3(F)

print_matrix(F, "F")

AT = [[A[j][i] for j in range(n)] for i in range(n)]
FA = [[F[i][j] + A[i][j] for j in range(n)] for i in range(n)]
FATP = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            FATP[i][j] += FA[i][k] * AT[k][j]

KF = [[K * F[i][j] for j in range(n)] for i in range(n)]

result = [[FATP[i][j] - KF[i][j] for j in range(n)] for i in range(n)]

print_matrix(AT, "AT")
print_matrix(FATP, "(F+A)*AT")
print_matrix(KF, "K*F")
print_matrix(result, "(F+A)*AT - K*F")
