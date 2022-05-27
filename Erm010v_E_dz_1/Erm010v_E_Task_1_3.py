# GU_python_2557
# Task_1_3
# Date_20_05_22

for i in range (1, 101):
    w = "процент"
    if (i % 10) == 1 and i != 11:
        print(i, w)
    elif 1 < (i % 10) <=4:
        if 10 < i <= 14:
            print(i, w + "ов")
        else:
            print(i, w + "а")
    else:
        print(i, w + "ов")

