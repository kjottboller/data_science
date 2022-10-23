# Guess the number game
# A computer guessing n choosing a number

import numpy as np

number = np.random.randint(1, 100)
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
        break
        