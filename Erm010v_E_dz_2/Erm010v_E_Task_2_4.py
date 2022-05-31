# GU_python_2557
# Task_2_4
# Date_31_05_22

numbs = [57.8, 46.51, 97, 44.44, 33.33, 55.55, 66.66, 100, 2000, 999]
numbs.sort()
for numb in numbs:
    rur = int(numb)
    kop = (numb - int(numb)) * 100
    print(f'{rur}руб. {kop:02.0f}коп.')


#--------------------- For practice ----------------
#    # Вывод списка товаров
#    elif choice == "1":
#        print("Список товаров:\n")
#        print("Код:\tНаименование:\tФирма-производитель:\tВозр.ограничение:\tЦена:")
#        for entry in toys:
#            code, name, firm, age, price = entry
#            print(code, "|", name, "|", firm, "|", age, "|", price, "\t")



#--------------------- For practice ----------------
#toys = []  # Список где хранятся товары

#choice = None  # Пункт меню
#while choice != "0":  # Пока выбор не равен "0"

#    print(
#        """
#        Магазин игрушек
#
#        0 - Выход
#        1 - Список товаров
#        2 - Добавить товар
#        3 - Поиск товара
#        """
#    )
#
#    choice = input("Ваш выбор: ")
#    print()
#
#    # Выход
#    if choice == "0":
#        print("До свидания.")
#
#    # Вывод списка товаров
#    elif choice == "1":
#        print("Список товаров:\n")
#        print("Код:\tНаименование:\tФирма-производитель:\tВозр.ограничение:\tЦена:")
#        for entry in toys:
#            code, name, firm, age, price = entry
#            print(code, "|", name, "|", firm, "|", age, "|", price, "\t")
#
#    # Добавление товара
#    elif choice == "2":
#        name = input("Введите наименование товара: ")  # Наименование
#        code = int(input("Введите код товара: "))
#        firm = input("Введите фирму-производитель: ")
#        age = int(input("Введите возраст.ограничение: "))
#        price = int(input("Введите стоимость товара: "))
#       entry = (code, name, firm, age, price)
#        toys.append(entry)  # Добавление к концу строки
#        toys.sort(reverse=True)  # Сортировка по убыванию
#
#
#    # Поиск товара
#    elif choice == "3":
#        search = input("Введите слово, которое вы хотите найти: ")
#        if search in entry:
#            toys = entry[search]
#            print("\n", toys)
#    # В случае другого выбора
#    else:
#        print("Извните, но", choice, "не является корректным пунктом.")


