def swap_pairs(s):
    res = ""
    for i in range(0, len(s) - 1, 2):
        res += s[i + 1] + s[i]
    if len(s) % 2 != 0:
        res += s[-1]
    return res

def swap_every_other_pair(s):
    res_list = list(s)
    for i in range(0, len(res_list) - 1, 4):
        if i + 1 < len(res_list):
            res_list[i], res_list[i + 1] = res_list[i + 1], res_list[i]
    return "".join(res_list)

def process_numbers(filename="C:\\Users\\vadim\\OneDrive\\Desktop\\laba\\lab3\\rannum.txt"):
    processed_numbers = {}
    three_zeros_encountered = False
    last_number_str = ""

    try:
        with open(filename, 'r') as file:
            numbers_str = file.read().split()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    for num_str in numbers_str:
        try:
            num = int(num_str)
            num_str = str(num)
            last_number_str = num_str

            if "000" in num_str:
                three_zeros_encountered = True

            if num_str in processed_numbers:
                result = processed_numbers[num_str]
            else:
                if three_zeros_encountered:
                    result = swap_every_other_pair(num_str)
                else:
                    result = swap_pairs(num_str)
                processed_numbers[num_str] = result

            print(result) # Вывод обработанного числа

        except ValueError:
            pass

    numbers_dict = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }

    # Обработка последнего числа после цикла
    if three_zeros_encountered:
        last_number_processed = swap_every_other_pair(last_number_str)
    else:
        last_number_processed = swap_pairs(last_number_str)

    last_number_words = ""
    for digit in last_number_processed:  # Используем обработанное число
        last_number_words += numbers_dict[digit] + " "

    print(f"Последнее число - {last_number_words.strip()}")

process_numbers()
