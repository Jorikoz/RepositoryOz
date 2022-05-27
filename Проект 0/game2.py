""" New game "Guess a number" компьютер загадвыет и сам отгадывает число"""
import numpy as np

def random_predict(number:int=1)-> int:
    """функция рандомно отгадывает число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101) #рандомно генерирует предполагаемое число
        if number == predict_number:
            break #выходим, если угадали
    return (count) #возвращаем количество попыток

# print(f' количество попыток: {random_predict(10)}')

def score_game(random_predict)->int:
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
        count_ls.append(random_predict(number)) #добавляем в лист решения функции рандомного поиска по списку из 1000 чисел
    score = int(np.mean(count_ls)) # находим среднее количество попыток при помощи функции из библиотеки numpy
    
    print(f' ваш алгоритм угадывает число в среднем за: {score} попыток')  
    return(score)

#RUN
score_game(random_predict)
  