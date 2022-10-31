# Guess the number
# A computer guessing n choosing a number

print('--------------------')

import numpy as np
number = np.random.randint(1, 101)

def random_predict(number):
    count_1 = 0
    min_num, max_num = 1, 101
    predict_number = int(np.random.randint(1, 101))
    
    while predict_number != number:
        count_1 += 1
        if predict_number > number:
           max_num = predict_number 
           predict_number = (max_num + min_num) // 2 
        elif predict_number < number:
           min_num = predict_number 
           predict_number = (max_num + min_num) // 2 
        else:
            break
    return count_1
print(f"Number of attempts (1): {random_predict(number)}")

print('. . .')

def own_algorithm(random_predict):
    count_2 = []
    np.random.seed(1)
    random_array = np.random.randit(1, 101, size = (1000))
    
    for number in random_array:
        count_2.append(int(random_predict(number)))
    
    score = int(np.mean(count_2))
    print(f"Your algorithm guessing in an average of {score} attempts!")
    return(score)
print(f"Number of attempts (2): {random_predict(10)}")

print('--------------------')
