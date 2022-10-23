# Guess the number game (2)
# A computer guessing n choosing a number

import numpy as np
number = np.random.randint(1, 101)
def random_predict(number):
    count_1 = 0
    mn = 1
    mx = 101
    while True:
        count_1 += 1
        md = (mn + mx) // 2  
        if md > number:
            mx = md
        elif md < number:
            mn = md
        else:
            print(f"The computer guessed the number in {count_1} attempts! This is the number {number}.")
            break 
    return count_1
print(f'Number of attempts: {random_predict(number)}')

print('----------------')

def algorithm(random_predict):
    count_2 = 0
    np.random.seed(1)
    random_numbers = np.random.randit(1, 101, size = (1000))
    for number in random_numbers:
        count_2.append(int(random_predict(number)))
    score = int(np.mean(count_2))
    print(f"Your algorithm guessing in an average of {score} attempts!")
    return score
print(f"Number of attempts: {random_predict(number)}")
    
