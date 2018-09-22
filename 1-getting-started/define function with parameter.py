def hello(name): # в случае вызова функции без параметра hello() функция вернет ошибку
    print("Hello,", name)

hello("Sashka") # "Sashka" -- фактический параметр

def hello(name = "World"): # задан параметр по умолчанию
    print("Hello,", name)

hello("Sashka") # "Sashka" -- фактический параметр

# Нормальная функция всю свою суть получает через параметры.




def max2(x = 1, y = 2):
    if x > y:
        return x # вернуть икс, если это максимум из двух параметров. ВНИМАНИЕ: РЕТЕРН прекращает выполнение функции. Дальше писать код на выполнение не надо.
    else:
        return y
    #или просто
    #return y

def max3(x = 1, y = 2, z = 3):
    return max2(x, max2(y,z)) # вычисляем большее из трех через ранее заданную функцию большего из двух

print(max3()) # 3
print(max3('ab','ba','bc')) #bc #в качестве аргументов используются стринги из букв. Используется утиная типизация для определния сравнимости стрингов по лексикографическом порядку (первая буква, вторая буква)


# meters to feet converter
def converter(original, coefficient):
    return original * coefficient

print(converter(10, 0.3048))



# meters to feet converter with default parameter
def converter(original, coefficient=0.3048):
    return original * coefficient

print(converter(10))


# meters to feet converter with changed default parameter (kilometers to miles)
def converter(original, coefficient=0.3048):
    return original * coefficient

print(converter(10, 1.6))


#Celsius to Fahrenheit converter
def converter(input):
    x = input * (9/5) + 32
    return input * x

#Celsius to Fahrenheit converter2
def converter(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit



# Обработка исключения
def string_length(mystring):
     if type(mystring) == int:
         return "Sorry, integers don't have length"
     elif type(mystring) == float:
         return "Sorry, floats don't have length"
     else:
         return len(mystring)
