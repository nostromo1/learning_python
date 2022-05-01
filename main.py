HELP = """"
help - напечатать справку по программе.
add - добавить задачу в список(название задачи запрашиваем у пользователя).
show - напечатать добавленные задачи."""

today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату: ")
        if date == 'Сегодня':
            print(today)
        elif date == 'Завтра':
            print(tomorrow)
        elif date == 'Остальное':
            print(other)
        else:
            print("Повторите ввод даты")
    elif command == "add":
        date = input("Введите дату задачи: ")
        task = input("Введите название задачи: ")
        if date == 'Сегодня':
            today.append(task)
            print("Задача добавлена")
            print(today)
        elif date == 'Завтра':
            tomorrow.append(task)
            print("Задача добавлена")
            print(tomorrow)

        elif date == 'Завтра':
            other.append(task)
            print("Задача добавлена")
            print(other)
    elif command == "exit":
        print("Спасибо за использование!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")