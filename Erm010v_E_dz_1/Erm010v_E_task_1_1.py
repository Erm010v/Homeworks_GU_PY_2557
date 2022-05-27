# GU_python_2557
# Task_1_1
# Date_20_05_22

duration = 400153
d_d = duration // (3600 * 24)
d_h = duration // 3600 % 24
d_m = duration // 60 % 60
d_s = duration % 60

if d_d != 0:
    print(f'{d_d} дн {d_h} час {d_m} мин {d_s} сек')
elif d_d == 0 and d_h != 0:
    print(f'{d_h} час {d_m} мин {d_s} сек')
elif d_d == 0 and d_h == 0 and d_m != 0:
    print(f'{d_m} мин {d_s} сек')
else:
    print(f'{d_s} сек')

#----First attempt----
#duration = 53
#s = duration % 60
#print(f'{s} секунды')

#duration = 153
#m = duration // 60
#s = duration % 60
#print(f'{m} минут {s} секунд')

#duration = 4153
#h = duration // 3600
#m = (duration - 3600) // 60
#s = duration % 60
#print(f'{h} час {m} минут {s} секунд')

#duration = 400153
#d = duration // 86400
#h = (duration - (86400 * d)) // 3600
#print(f'{d} дня {h} часов {m} минут {s} секунд')







