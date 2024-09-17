import datetime

def input_info():
    name = input('Введите название заметки: ')
    text = input('Введите тело заметки: ')
    data = datetime.datetime.now().strftime('%Y-%m-%d; %H-%M')

    return name, text, data
