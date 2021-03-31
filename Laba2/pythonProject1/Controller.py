import psycopg2
from View import *
from Model import *


def menu():
    flag = True
    conn = psycopg2.connect(database='firm', user='postgres', password='6213', host='localhost', port=5432)
    cursor = conn.cursor()
    while flag:
        print(" Enter:\n 1 - for testing task\n 2 - for task 2\n 3 - for 3\n 4 - exit\n")
        item = int(input())
        if item == 1:
            flag_1 = True
            while flag_1:
                print(" Enter:\n 1 - create\n 2 - delete \n 3 - edit\n 4 - get\n 5 - return to main menu\n")
                item_1 = int(input())
                if item_1 == 5:
                    flag_1 = False
                    continue
                if item_1 == 1:
                    (table, param1, param2) = menu_task1_create()
                    create(cursor, table, param1, param2)
                elif item_1 == 2:
                    (table, param) = menu_task_1_delete()
                    delete(cursor, table, param)
                elif item_1 == 3:
                    (table, param1, param2, param3) = menu_task_1_edit()
                    edit(cursor, table, param1, param2, param3)
                elif item_1 == 4:
                    table = menu_task_1_print()
                    print_table(cursor, table)
        elif item == 2:
            (table, number) = menu_task_2()
            random_generation(cursor, table, number)
        elif item == 3:
            (param, item_3) = menu_task_3()
            select_function(cursor, param, item_3)
        elif item == 4:
            flag = False
        else:
            print("\nFalse number\n")
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    menu()
