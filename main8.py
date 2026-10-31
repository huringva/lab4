t = int(input('Введите текущий час: '))

if t<4: print('Сейчас ночь')
elif t<12:print('Сейчас утро')
elif t<16: print('Сейчас день')
elif t<22: print('Сейчас вечер')
elif t>24:print('Некорректное время')
else: print('Сейчас ночь')
