#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите общее количество монет: '))
g = int(input('Введите количество монет лежащих гербом вверх '))
r = n - g
if g > r:
    print(f'Нужно перевернуть {r} монет.')
else:
    print(f'Нужно перевернуть {g} монет.')