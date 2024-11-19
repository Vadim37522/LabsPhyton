def read_matrix_from_file(filepath, encoding='utf-8'):
    """Чтение матрицы из файла, обработка ошибок кодировки."""
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            matrix = []
            for line in file:
                row = line.strip().split()
                numeric_row = []
                for num_str in row:
                    try:
                        numeric_row.append(float(num_str))
                    except ValueError:
                        print(f"Ошибка преобразования '{num_str}' в число.")
                        return None
                matrix.append(numeric_row)
            return matrix
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.")
        return None
    except UnicodeDecodeError:
        print(f"Ошибка декодирования файла '{filepath}'. Проверьте кодировку (указана: {encoding}).")
        return None


def transpose_matrix(matrix):
    """Транспонация матрицы."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def count_zeros(matrix, start_row, start_col, rows, cols):
    """Подсчет количество нулей в области."""
    count = 0
    for i in range(start_row, start_row + rows):
        for j in range(start_col, start_col + cols):
            if matrix[i][j] == 0:
                count += 1
    return count


def swap_regions(matrix, region1_start_row, region1_start_col, region2_start_row, region2_start_col, rows, cols, symmetric):
    """Свап области матрицы."""
    for i in range(rows):
        for j in range(cols):
            row1 = region1_start_row + i
            col1 = region1_start_col + j
            if symmetric:
                row2 = len(matrix) - 1 - row1
                col2 = len(matrix[0]) - 1 - col1
            else:
                row2 = region2_start_row + i
                col2 = region2_start_col + j
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]


def matrix_operation(F, A, K):
    """ (F + A) * AT - K * F."""
    AT = transpose_matrix(A)
    rows = len(F)
    cols = len(F[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            sum_FA = F[i][j] + A[i][j]
            dot_product = 0
            for k in range(cols):
                dot_product += sum_FA * AT[k][j] 
            result[i][j] = dot_product - K * F[i][j]
    return result


def print_matrix(matrix):
    """Вывод матрицы в консоль, форматируя числа как целые."""
    for row in matrix:
        print(' '.join(map(lambda x: str(int(x)), row))) 

filepath = r"C:\Users\vadim\OneDrive\Desktop\laba\lab1\Matrixx.txt"
A = read_matrix_from_file(filepath, encoding='utf-8')
K = 2

if A is None:
    exit() 

print("Матрица A:")
print_matrix(A)

F = [row[:] for row in A]

zeros_region1 = count_zeros(F, 0, 0, 3, 3)
zeros_region3 = count_zeros(F, 3, 0, 3, 3)

if zeros_region1 > zeros_region3:
    swap_regions(F, 0, 0, 0, 3, 3, 3, True)
else:
    swap_regions(F, 0, 0, 0, 3, 3, 3, False)

result_matrix = matrix_operation(F, A, K)

print("\nМатрица F:")
print_matrix(F)

print("\nРезультат (F+A)*AT - K*F:")
print_matrix(result_matrix)


