def number_divisors(number):            #Функция которая находит все делители числа (кроме 1)
    list_of_divisors = []
    for i in range(2, number + 1):
        if number % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors


def required_password_searching(number):   #Функция которая подбирает пароли, чтобы исключить пары типа: 12 и 21.
    divisors = number_divisors(number)     #Перебор первого числа пароля не превосходит половины числа + 1
    password = ''
    for j in range(1, (divisors[-1] // 2) + 1):
        for k in range(j + 1, divisors[-1]):
            if divisors[-1] % (j + k) == 0 and j != k:
                password += str(j) + str(k)
    return password


def test_of_programm(test_dict):            #Дальше код для своей личной проверки, я решил его оставить
    for key in test_dict:            #Вдруг будет интересно, данные для проверки брал с описания задания
        if int(required_password_searching(key)) == test_dict[key]:
            print(f'{key} -True')
        else:
            print(f'{key} -False')


TEST_DICT = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746,
             11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968,
             15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089,
             18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
             20: 13141911923282183731746416515614713812911}

for i in range(3, 21):
    print(f'{i}: {required_password_searching(i)} ')

test_of_programm(TEST_DICT)
