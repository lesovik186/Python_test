# Friend or Foe?: (Задача в принцепе решена, но тест не проходит, нужно определить входной аргумент через def ......)

a = ["Ryan", "Jimmy", "abc", "d", "Cool Man"]

b = list(filter(lambda x: len(x) == 4, a))
# print(b)

# Friend or Foe?:  (тесты прошёл)

def friend(x):
    h = list(filter(lambda m: len(m) == 4, x))
    return h


# print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))


# How Many Streets?: (Пока что эта задача не решена)

# def count_streets(streets, drivers):
    # sub_array = []
    # k = 0
    # for street in streets:
    #     print(street)
    # for i in drivers:
    #     i = list(i)
    #     print(i)

# count_streets(["first", "second", "third", "fourth", "fifth", "sixth", "seventh"],[("first", "second"), ("second", "seventh"), ("sixth", "fourth")])


# How many e-mails we sent today?:   (Тесты прошёл)

import math
def get_percentage(sent=2, limit=1000):  # два аргумента не обязательные, если введён только один аргумент - приоритет к использованию у первого
    if sent == 0:
        return "No e-mails sent"
    if sent >= limit:
        return "Daily limit is reached"
    else:
        x = sent * 100 / limit  # расчёт процентов
        res = math.floor(x)  # округление чисел в меньшую сторону
        res = str(res)
        return res + '%'


# print(get_percentage(0, 1000))

# Exes and Ohs:  (Тесты пройдены)

def xo(s):
    a = s.count('x')
    b = s.count('X')
    c = s.count('o')
    d = s.count('O')
    ab = (a + b)
    cd = (c + d)
    return True if ab == cd else False


# print(xo("xOXxoo"))

# Blood Moon: (тесты прошёл)

def blood_moon(r):    # Решение математическое (с геометрическим рисунком) есть на листках бумаги А4
    cd = r
    ac = cd
    ad = math.sqrt(ac**2 + cd**2)
    ae = ad / 2
    fe = ae
    af = math.sqrt(ae**2 + fe**2)
    s_ahfdea = (3.14 * ae**2)/2
    s_ahfea = s_ahfdea / 2
    s_afe = ae * fe / 2
    s_ahfa = s_ahfea - s_afe
    s_agfa = (3.14 * (af * 0.5) ** 2)/ 2
    s_moon = s_agfa - s_ahfa
    return round(s_moon, 2)


# print(blood_moon(3))

# Drone Fly-By:   (Тесты пройдены)

def fly_by(lamps, drone):
    a = drone.count('=')    # находим количество этого элемента в аргументе drone
    lamp_new = lamps.replace('x', 'o', a + 1)   # создадим переменную lamp_new, в ней будет изменённая строка lamps, x меняем на o, (a + 1)- число замен слева- направо.
    # число замен должно быть на один больше чем символов =
    return lamp_new


# print(fly_by('xxxxxxxxxxxxxxx', '==========T'))


# Sum of angles:  (Тесты пройдены)

def angle(n):
    sum = 180 * (n - 2)
    return sum


# print(angle(5))


# Sum of two lowest positive integers:  (Найти сумму двух минимальных чисел массива)  (Задача прошла тесты)

def sum_two_smallest_numbers(numbers):
    numbers.sort(reverse=True)   # сортируем массив по убыванию
    min_first = min(numbers)
    a = min_first
    numbers.remove(min_first)  # удаляем из массива самое минимальное число (первое), чтобы считать второе минимальное число
    min_second = min(numbers)
    summing = min_second + a  # суммируем два найденных самых минимальных чисел из массива
    return summing


# print(sum_two_smallest_numbers([25, 42, 12, 20, 22]))

# Longest vowel chain:

def solve(s):             # это "вступление" к задаче, тут просто посчитал количество гласных в строке
    letters = 'aeiouyAEIOUY'
    counter = 0
    for i in s:
        # print(i)
        if i in letters:
            counter += 1
    return counter


# print(solve("codewarriors"))


# Найти наибольшую подстроку неповторяющихся символов в строке:  (похожая задача к моей, но объяснение в youtube плохое)

def solve2(s):
    res = 0
    start = 0
    w = set()  # храним тут текуще заходящее значение
    for el in s:
        while el in w:
            w.remove(s[start])
            start += 1
        w.add(el)
        res = max(res, len(w))
    return res


# print(solve2("bacabcbb"))  # выход --> 3


# Longest vowel chain:    (задача выполнена, тесты корявые: Test выполны, Attempt - выполнены наполовину)

def solve3(s):          # решение этой задачи - стандартный алгоритм.  Объяснение есть на бумаге А4
    letters = 'aeiouyAEIOUY'
    k = km = 0
    for i in range(len(s)):
        if s[i] in letters:
            k += 1
            km = max(k, km)
        else:
            k = 0
    return km


# print(solve3("oaoeiiYFBWWUIEAOfoeeu"))

# Pairs of integers from n to n:   (Тесты прошёл)   Объяснение есть на бумаге А4

def generate_pairs(m, n):
    s = [(a, b) for a in range(m, n + 1) for b in range(m, n + 1) if m <= a <= b <= n]  # создал генератор списка
    return s


# print(generate_pairs(2, 4))   # [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


# Sqre Every Digit:   (Тесты пройдены)

def square_digits(num):
    if num == 0:
        return 0
    else:
        num_new = str(num)      # преобразуем аргумент в строку
        num_new2 = num_new[:: -1]  # строку-число разворачиваем (так на выходе соблюдается правильность условия задачи)
        if num_new2[0] == '0':       # это случай, когда входное число заканчивается нулём (нужно не потерять этот ноль в процессе преобразований)
            num_new3 = int(num_new2)
            print(num_new3)
            b = []            # Далее идёт реализация операция mod - это получение остатка от деления (есть описание на А4)
            while num_new3 != 0:
                p = num_new3 % 10
                a = p ** 2
                num_new3 = num_new3 // 10
                b.append(a)
            ll = (''.join([str(i) for i in b]))  # это команда-вывод (есть описание на А4)
            res = ll + '0'  # добавляем в конце к полученному числу "0" который был утерян в ходе преобразования
            result = int(res)  # избавляемся от кавычек в ответе чтобы удовлетворить тесты

            return result

        elif num_new2[0] != 0:    # это уже более частый случай когда входное число не заканчивается нулём и выполнение идёт почти так же как
            num_new3 = int(num_new2)  # ветка выше, только тут в конце не нужно к числу добавлять ноль
            print(num_new3)
            b = []
            while num_new3 != 0:
                p = num_new3 % 10
                a = p ** 2
                num_new3 = num_new3 // 10
                b.append(a)
            res = (''.join([str(i) for i in b]))
            result = int(res)

            return result


# print(square_digits(28))


# Find the smallest power higher than a given a value:   (Тесты пройдены)

def find_next_power(val, pow_):        # Объяснение есть на бумаге А4
    m = val ** (1/pow_)
    z = math.floor(m)
    res = (z + 1) ** pow_
    return res


# print(find_next_power(12385, 3))

# Collision Detection:     (Тесты пройдены)


def collision(x1, y1, radius1, x2, y2, radius2):
    c = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # тут, 'c' это расстояние между центрами окружностей
    if c <= radius1 or c <= radius2 or c <= radius1 + radius2:   # это те условия, когда окружности сталкиваются между собой (соприкосаются)
        return True
    else:
        return False


# print(collision(-5, 5, 5.0001,5, -5, 5*math.sqrt(5)))

# Reverse words:    (Полностью решение этой задачи нашёл в Интернете. Тесты пройдены)


def reverse_words2(text):
    nt = ''
    w = ''
    zap = 0
    for i, s in enumerate(text):  # i -->  0 1 2 3 ..... 19 20; s -->  d o u b l e  s p a c e d  w o r d s (проходит итерацию)
        if s != ' ':
            zap = 1   # т. е. если элемент 's' не пробел, тогда этот символ попадает в переменную-накопитель 'w'
            w += s
            if i == len(text) - 1:  # проитерировалась вся строка
                nt += w[::-1]
        else:             # иначе (элемент 's' пробел)
            zap = 0
            nt += w[::-1]
            w = ''
            nt += ' '

    return nt


print(reverse_words2('double  spaced  words'))
