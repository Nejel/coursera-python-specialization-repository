#Way 1

numbers = [1, 2, 3]
file = open("numbers.txt", "w")
for i in numbers:
     file.write(str(i) + "\n")
file.close()



#Way 2 Способ записи в файл

temperatures = [10,-20,-289,100]

def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")

writer(temperatures, "temps.txt") #Here we're calling the function



#Way 3
#Открываем три файла, конкатенируем содержимое и пишем в новый файл с таймштампом

import glob2
from datetime import datetime

filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")
