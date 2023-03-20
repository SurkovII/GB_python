# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных


def importFile(user):
    with open("file.txt", "a") as file:
        file.write(user + "\n")

def exportFile():
    with open("file.txt", "r") as f:
        a = f.readlines()
        a = [i.strip() for i in a]
        return a

def find_user(lst, str):
    result =[]
    for value in lst:
        if str in value:
            result.append(value.strip())
    return result

def table_user(lst):
    count = 1
    for value in lst:
        print(count, value)
        count +=1
        
def get_del_user(lst, int):
    res_list = ""
    for i in range(len(lst)):
        if i == int-1:
            res_list = lst[i]
    return res_list

def del_user(list_user, lst):
    out_list = []
    for data in lst:
        if data != list_user:
            out_list.append(data)
    return out_list

def write_data(lst):
    file = open("file.txt", "w")
    for data in lst:
        file.write(data+"\n")
        
def change_user(change_User, new_User , lst):
    out_list = []
    for data in lst:
        if data != change_User:
            out_list.append(data)
        else:
            out_list.append(new_User)      
    return out_list
