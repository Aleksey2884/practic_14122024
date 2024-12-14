while 1 > 0: # True 'начало цикла'
    number = int(input('Введите число'))
    if number % 2 == 0:
        print('число чётное')
        continue
    else:
        print('число нечётное')
        break # 'останавливает цикл'