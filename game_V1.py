# GUESS THE NUMBER???
import numpy as np

number = np.random.randint(1, 100) # загадываем число
count = 0 # количество попыток

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Число должно быть меньше!")
    elif predict_number < number:
        print("Число должно быть больше!")
    else:
        print(f"Вы угадали число за {count} попыток! Это число = {number}")
        break # конец игры и выход из цикла
        