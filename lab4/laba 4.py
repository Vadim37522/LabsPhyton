import re

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

def number_to_words(number_str):
    replacements = [
        (r'0', 'ноль '), (r'1', 'один '), (r'2', 'два '), (r'3', 'три '),
        (r'4', 'четыре '), (r'5', 'пять '), (r'6', 'шесть '), (r'7', 'семь '),
        (r'8', 'восемь '), (r'9', 'девять ')
    ]
    
    words = number_str
    for pattern, replacement in replacements:
        words = re.sub(pattern, replacement, words)
    return words.strip()

def process_numbers(filename="C:\\Users\\vadim\\OneDrive\\Desktop\\laba\\lab4\\rannum.txt"):
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
            
            if re.search(r"000", num_str):
                three_zeros_encountered = True

            if three_zeros_encountered:
                processed_number = swap_every_other_pair(num_str)
            else:
                processed_number = swap_pairs(num_str)
            print(processed_number)
        
        except ValueError:
            pass

    if three_zeros_encountered:
        last_number_processed = swap_every_other_pair(last_number_str)
    else:
        last_number_processed = swap_pairs(last_number_str)

    last_number_words = number_to_words(last_number_processed)
    print(f"Последнее число - {last_number_words}")

process_numbers()
