import math
import time
from tabulate import tabulate



def factorial(n):
    """Вычисляет факториал числа n итеративно."""
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result



def recursive_f(n):
    """
    Вычисляет F(n) рекурсивно.
    Если n = 0, возвращает 5.
    Если n = 1, возвращает 1.
    Иначе вычисляет значение по формуле, вызывая саму себя.
    """
    if n == 0:
        return 5
    elif n == 1:
        return 1
    else:
        
        return ((-1) ** n) * (2 * recursive_f(n - 1) / factorial(n) +
                             recursive_f(n - 2) / factorial(2 * n))



def iterative_f(n):
    
    if n == 0:
        return 5
    elif n == 1:
        return 1

    f_values = [5, 1]  

    for i in range(2, n + 1):
        
        f_n = ((-1) ** i) * (2 * f_values[i - 1] / factorial(i) + f_values[i - 2] / factorial(2 * i))
        f_values.append(f_n)
    return f_values[n]  



def test_functions(n_values, runs=5):
    
    results = []
    for n in n_values:
       
        recursive_times = []
        for _ in range(runs): 
            start_time = time.time()
            recursive_f(n)
            end_time = time.time()
            recursive_times.append(end_time - start_time)
        average_recursive_time = sum(recursive_times) / runs if recursive_times else 0

      
        iterative_times = []
        for _ in range(runs):  
            start_time = time.time()
            iterative_f(n)
            end_time = time.time()
            iterative_times.append(end_time - start_time)
        average_iterative_time = sum(iterative_times) / runs if iterative_times else 0

        
        results.append([n, average_recursive_time, average_iterative_time])

   
    headers = ["N", "Рекурсия (с)", "Итерация (с)"]
    print(tabulate(results, headers=headers, tablefmt="grid"))



if __name__ == "__main__":
    n_values = [3, 5, 7, 10, 12, 15, 20, 25]  # Разные значения n
    print("Сравнение рекурсивной и итеративной функции:")
    test_functions(n_values)
