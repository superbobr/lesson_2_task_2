HELP = '''
help - напечатать справку по программе
add - добавить задачу в список
show - напечатать все добавленные задачи'''

today = []
tomorrow = []
other = []

run = True

while run:
  command = input('Введите команду: ')
  if command == 'help':
    print(HELP)
  elif command == 'show':
    print('Сегодня: {}, Завтра: {}, Другие дни {}'.format(today, tomorrow, other))
  elif command == 'add':
    user_date = input('Введите дату задачи: ')
    task = input('Введите название задачи: ')
    if user_date == 'Сегодня':
      today.append(task)
      print('Задача добавлена')
    elif user_date == 'Завтра':
      tomorrow.append(task)
      print('Задача добавлена')
    else:
      other.append(task)
      print('Задача добавлена')
    
  elif command == 'exit':
    print('Спасибо за использование! До свидания!')
    run = False
  else:
    print('Неизвестная команда')
    print('До свидания!')
    run = False