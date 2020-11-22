A = True
while A == True:
    print('Введите значения k, l, m, n. Обратите внимание, что цифры должны находится в промежутке от 0 до 8!')
    k = input('Введите значение k: ')
    l = input('Введите значение l: ')
    m = input('Введите значение m: ')
    n = input('Введите значение n: ')
    if not k.isdigit() or int(k) < 1 or int(k) > 8 or not l.isdigit() or int(l) < 1 or int(l) > 8 or not m.isdigit() or int(m) < 1 or int(m) > 8 or not n.isdigit() or int(n) < 1 or int(n) > 8:
        print('Введенные данные не соответствуют требованиям!')
        A = True
    else:
        k = int(k)
        l = int(l)
        m = int(m)
        n = int(n)
        A = False


def square_colour(k,l,m,n):

    print('\n1.Являются ли поля (k, l) и (m, n) полями одного цвета?')

    if (k + l) % 2 == (m + n) % 2:
        if (k + l) % 2 == 0:
            print('Да, оба поля чёрные!')
        else:
            print('Да, оба поля белые!')
    else:
        if (k + l) % 2 == 0:
            print('Нет, поле (k,l) — чёрное, а поле (m,n) — белое!')
        else:
            print('Нет, поле (k,l) — белое, а поле (m,n) — чёрное!')


def queen(k,l,m,n):

    print('\n2.На поле (k, l) расположен ферзь. Угрожает ли он полю (m, n)?')

    if k == m or l == n or abs(k - m) == abs(l - n):
        print('Да, угрожает!')
    else:
        print('Нет, не угрожает!')


def knight(k,l,m,n):

    print('\n3.На поле (k, l) расположен конь. Угрожает ли он полю (m, n)?')

    if (k + 2) == m or (k - 2) == m:
        if (l + 1) == n or (l - 1) == n:
            print('Да, угрожает!')
        else:
            print('Нет, не угрожает!')
    elif (l + 2) == n or (l - 2) == n:
        if (k + 1) == m or (k - 1) == m:
            print('Да, угрожает!')
        else:
            print('Нет, не угрожает!')
    elif (k + 1) == m or (k - 1) == m:
        if (l + 2) == n or (l - 2) == n:
            print('Да, угрожает!')
        else:
            print('Нет, не угрожает!')
    elif (l + 1) == n or (l - 1) == n:
        if (k + 2) == m or (k - 2) == m:
            print('Да, угрожает!')
        else:
            print('Нет, не угрожает!')


def rook(k,l,m,n):

    print('\n4.Можно ли с поля (k, l) одним ходом ладьи попасть на поле (m, n)?')

    if k == m or l == n:
        print('Да, можно!')
    else:
        if k > m:
            while k != m:
                k -= 1
            print(f'Нет, двигайтесь влево пока не достигните клетки {k, l}!')
        else:
            while k != m:
                k += 1
            print(f'Нет, двигайтесь вправо пока не достигните клетки {k, l}!')


def queen_moves(k,l,m,n):

     print('\n5.Можно ли с поля (k, l) одним ходом ферзя попасть на поле (m, n)?')

     if (k + l) % 2 == (m + n) % 2:
         if k == m or l == n or abs(k - m) == abs(l - n):
             print('Да, можно!')
         else:
             if k > m:
                 while k != m:
                     k -= 1
                 print(f'Нет, двигайтесь влево пока не достигните клетки {k, l}!')
             elif k < m:
                 while k != m:
                     k += 1
                 print(f'Нет, двигайтесь вправо пока не достигните клетки {k, l}!')
         x = (k + l + m - n) // 2
         y = (k + l - m + n) // 2
         if x > 8 or x < 1 or y > 8 or y < 1:
             x = (m + n + k - l) // 2
             y = (m + n - k + l) // 2
         print(f'Либо двигайтесь по диагонали на ячейку {x, y}!')
     else:
         if k == m or l == n or abs(k - m) == abs(l - n):
             print('Да, можно!')
         else:
             if k > m:
                 while k != m:
                     k -= 1
                 print(f'Нет, двигайтесь влево пока не достигните клетки {k, l}!')
             elif k < m:
                 while k != m:
                     k += 1
                 print(f'Нет, двигайтесь вправо пока не достигните клетки {k, l}!')


def bishop(k,l,m,n):

    print('\n6.Можно ли с поля (k, l) одним ходом слона попасть на поле (m, n)?')

    if (k + l) % 2 == (m + n) % 2:
        if abs(k - m) == abs(l - n):
            print('Да, можно!')
        else:
            x = (k + l + m - n) // 2
            y = (k + l - m + n) // 2
            if x > 8 or x < 1 or y > 8 or y < 1:
                x = (m + n + k - l) // 2
                y = (m + n - k + l) // 2
            print(f'Нет, двигайтесь по диагонали на ячейку {x, y}!')
    else:
        print('Нельзя, поля разного цвета!')



if __name__ == "__main__":
    square_colour(k,l,m,n)
    queen(k,l,m,n)
    knight(k,l,m,n)
    rook(k,l,m,n)
    queen_moves(k, l, m, n)
    bishop(k, l, m, n)

