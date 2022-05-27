def random_predict(number:int=1) -> int:
    count = 0
    min = 1
    max = 101
    predict_number = (min+max)//2
    while True:
        count += 1
        if number > predict_number:
            min = predict_number + 1
            predict_number = (min + max)//2
        elif number < predict_number:
            max = predict_number
            predict_number = (min + max) // 2
        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return(count)