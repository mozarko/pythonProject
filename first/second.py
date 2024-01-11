def choose_plural(num, tpl):
    new_num = str(num)
    x_10 = new_num[-1]
    x_10 = int(x_10)
    if x_10 == 0:
        return f'{num} {tpl[2]}'
    if num <= 10:
        if x_10 == 1:
            return f'{num} {tpl[0]}'
        if 1 < x_10 <= 4:
            return f'{num} {tpl[1]}'
        if 5 <= x_10 <= 9 or x_10 == 0:
            return f'{num} {tpl[2]}'
    if num > 10:
        x_100 = new_num[-2] + new_num[-1]
        x_100 = int(x_100)
        if 11 <= x_100 <= 19:
            return f'{num} {tpl[2]}'
        if x_10 == 1:
            return f'{num} {tpl[0]}'
        if 1 < x_10 <= 4:
            return f'{num} {tpl[1]}'
        if 5 <= x_10 <= 9 or x_10 == 0:
            return f'{num} {tpl[2]}'


print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(23422, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(111, ('стул', 'стула', 'стульев')))
