def get_op():
    print("Выберите нужный пункт: 1 - импорт данных, 2 - экспорт данных, 3 - удаление данных, 4 - изменение данных ")
    op = input()
    return op
  
def get_User():
    print("Введите Фамилию, Имя и Телефон ")
    user = input()
    return user

def get_data():
    print("Введите данные для экспорта ")
    expData = input()
    return expData
    
def get_del_User():
    print("Введите данные, пользователя которого необходимо удалить ")
    del_User = input()
    return del_User

def num_del_User():
    print("Укажите номер человека, которого необходимо удалить ")
    num_User = input()
    return num_User

def change():
    print("Введите данные, пользователя которого необходимо изменить ")
    change_User = input()
    return change_User

def num_change_User():
    print("Укажите номер человека, которого необходимо изменить ")
    num_change_User = input()
    return num_change_User

def new_data_User():
    print("Введите измененные Фамилию, Имя и Телефон  ")
    new_User = input()
    return new_User