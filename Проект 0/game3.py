""" Test game "Guess a number ver3" компьютер загадвыет и сам отгадывает число меньше чем за 20 попыток"""
import numpy as np

def super_predict(number:int=1)-> int:
    """Функция отгадывает число бинарным методом

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    max = 101
    min = 1
    predict_number = (min+max)//2 #делим сумму на "//", чтобы было целое число в результате
    
    while True:
        count += 1 
        if number < predict_number:
            max = predict_number
            predict_number = (min+max)//2
        elif number > predict_number:
            min = predict_number
            predict_number = (min+max)//2
        else:
            print(f'ваш алгоритм нашел загаданное число за: {count} попыток. Это число {number}')
            break #выход из цикла. Конец игры
    return(count)

#RUN
#super_predict(33)


def score_game(super_predict)->int:
    """Функция подсчитывает количество попыток в среднем из 1000 подходов

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для производительности ЧТО ЭТО ВООБЩЕ?
    random_array = np.random.randint(1,101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(super_predict(number)) #добавляем в лист решения функции рандомного поиска по списку из 1000 чисел
    score = int(np.mean(count_ls)) # находим среднее количество попыток при помощи функции из библиотеки numpy
    
    print(f' ваш алгоритм угадывает число в среднем за: {score} попыток')  
    return(score)

#RUN
score_game(super_predict)

if __name__=='__main__':
    score_game(super_predict)