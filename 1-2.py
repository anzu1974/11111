
sec = int(input('Введите время в секундах - '))
#print(type(time_sec))
#print(f'Время в секундах - {time_sec}')

time_sec = sec - int(sec / 60)*60
time_min = int(sec / 60) - int(int(sec / 60) / 60) * 60
#print(int(sec / 60))
#print(int(int(sec / 60) / 60))
time_chas = int(int(sec / 60) / 60)

print(f'Перевод времени из {sec} сек. в часы составляет - {time_chas} час {time_min} мин {time_sec} сек')


