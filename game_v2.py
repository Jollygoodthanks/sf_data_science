import numpy as np

def random_predict(number:int=1) -> int:

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count

print(f"Number of tries: {random_predict()}")   

def score_game(random_predict) -> int:
    """ With which number of tries your program guesses the number
    Args:
        random_predict ([type]): guessing function

    Returns:
        int: mean number of tries 
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Your algorythm guesses the number with approximately: {score} tries')
    return(score)

# RUN
score_game(random_predict)
