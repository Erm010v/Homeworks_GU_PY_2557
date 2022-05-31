# GU_python_2557
# Task_2_2
# Date_31_05_22

weather_today = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = []
for i in range(len(weather_today)):
    if weather_today[i].startswith('+'):
        weather_today[i] = weather_today[i].zfill(3)
    elif weather_today[i].isdigit():
        weather_today[i] = weather_today[i].zfill(2)
result.extend(weather_today)
i = 0
while i < len(result):
    if result[i].isdigit() or result[i].startswith('+') and result[i][1:].isdigit():
        result.insert(i, '"')
        result.insert(i+2, '"')
        i += 2
    i += 1
print(result)
print(' '.join(result))


# ----------------------2 Option ------------------
#Weather_today = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
#def add_zero(text):
#   for item in range(len(text)):
#        if text[item].startswith('+'):
#            text[item] = text[item].replace('+','0')
#            text[item] = f'"+{text[item]}"'
#        if text[item].isdigit():
#            text[item] = f'"+{text[item].zfill(2)}"'
#    return ' '.join(text)
#
#print(id(Weather_today))
#print(add_zero(Weather_today))

# --------------------3 Option --------------------
#def get_sign(x):
#    if x[0] in '+-':
#        return x[0]

#weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

#i = 0
#while i < len(weather):
#    sign = get_sign(weather[i])
#    if weather[i].isdigit() or (sign and weather[i][1:].isdigit()):
#        if sign:
#           weather[i] = sign + weather[i][1:].zfill(2)
#        else:
#            weather[i] = weather[i].zfill(2)
#
#        weather.insert(i, '"')
#        weather.insert(i + 2, '"')
#        i += 2
#i += 1
#print(weather)
