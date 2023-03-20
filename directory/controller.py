from view import *
from ask import *
def main():
    while True:
        op = get_op()
        if op == "1":
            user = get_User()
            importFile(user)
        elif op == "2":
            list = exportFile()
            exp_user = get_data()
            lst = find_user(list, exp_user)
            table_user(lst)
            if len(lst) == 0:
                print("Нет искомых данных! Повторите ввод!")
            
        elif op == "3":
            data_del = get_del_User()
            list_del = exportFile()
            lst = find_user(list_del, data_del)
            table_user(lst)
            num_del = int(num_del_User())
            get_del = get_del_user(lst, num_del)
            write_data(del_user(get_del, list_del))

        elif op == "4":
            user_change = change()
            list_change = exportFile()
            lst = find_user(list_change, user_change)
            table_user(lst)            
            num_change = int(num_change_User())
            get_del = get_del_user(lst, num_change)
            new_User = new_data_User()
            write_data(change_user(get_del, new_User, list_change))                      
        else:
            break      
main()    