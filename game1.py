import random
число = random.randint(1,100)
while True:
    print('Вгадай число між 1 і 100')
    здогад = input()
    i = int(здогад)
    if i == число:
        print('Правильний здогад')
        break
    elif i < число:
        print('Бери вище')
    elif i > число:
        print('Бери нижче')
