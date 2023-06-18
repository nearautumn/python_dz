def get_new_id(phonebook: str) -> int:
    with open(phonebook, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        last_line = lines[-1]
        new_id = int(last_line[:(last_line.find(';'))]) + 1
        return new_id

def show_all_records(phonebook: str):
    ls = []
    with open(phonebook, 'r', encoding = 'utf-8') as f:
        for line in f:
            ls.append(line.strip())
        user_view = [d.replace(';', ' ') for d in ls]
        print(*user_view, sep = '\n')

def search_record(phonebook: str, contact_name: str) -> str:
    with open(phonebook, 'r', encoding='utf-8') as f:
        for line in f:
            if contact_name in line:
                return line.replace(';', ' ')

def add_contact(phonebook: str):
    with open(phonebook, 'a', encoding='utf-8') as f:
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        second_name = input('Введите отчество: ')
        phone_number = input('Введите номер телефона: ')
        record = '\n' + str(get_new_id(phonebook)) + ';' + surname + ';' + name + ';' + second_name + ';' + phone_number
        f.writelines(record)

def edit_record(phonebook: str):
    editing_id = input('Введите ID изменяемого контакта: ')
    list_phonebook = []
    with open(phonebook, 'r', encoding='utf-8') as f:
        list_phonebook = f.readlines()
    for i in list_phonebook:
        if i.startswith(editing_id):
            editing_record = i
    print ('Что Вы хотите изменить?', 
    '1 - Фамилия;',
    '2 - Имя;',
    '3 - Отчество;',
    '4 - Номер телефона;')
    user_select = int(input())
    new_contact_list = editing_record.split(';')
    if user_select == 1:
        new_contact_list[1] = input('Введите фамилию: ') 
    elif user_select == 2:
        new_contact_list[2] = input('Введите имя: ') 
    elif user_select == 3:
        new_contact_list[3] = input('Введите отчество: ') 
    elif user_select == 4:
        new_contact_list[4] = input('Введите номер телефона')
    new_record = ';'.join(new_contact_list)
    list_phonebook.append(('\n' + new_record))
    del list_phonebook[editing_record.index(editing_id)]
    with open (phonebook, 'w', encoding='utf-8') as f:
        f.writelines(list_phonebook)

def delete_record(phonebook: str):
    deleting_id = input('Введите ID удаляемого контакта: ')
    list_phonebook = []
    with open(phonebook, 'r', encoding='utf-8') as f:
        list_phonebook = f.readlines()
    for i in range(len(list_phonebook)):
        if list_phonebook[i].startswith(deleting_id):
            j = i
    del list_phonebook[j]
    with open (phonebook, 'w', encoding='utf-8') as f:
        f.writelines(list_phonebook)
    



   

