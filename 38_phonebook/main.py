from modules import *


def main():
    print('Выберите действие: 1 - Показать справочник', 
    '2 - Найти контакт',
    '3 - Добавить контакт',
    '4 - Изменить контакт',
    '5 - Удалить контакт')
    select = int(input())
    if select == 1:
        print('Ваши контакты: ')
        show_all_records(file_path)
    elif select == 2:
        name = input('Введите фамилию: ')
        print(search_record(file_path, name))
    elif select == 3:
        add_contact(file_path)
        print('Контакт добавлен!')
    # elif select == 4:
    #     show_all_records(file_path)
    #     edit_record(file_path)
    #     print('Контакт изменен!')
    elif select == 5:
        show_all_records(file_path)
        delete_record(file_path)
        print('Контакт удален!')
    else:
        print('Некорректный ввод')
        main()


file_path = 'file.txt'
main()