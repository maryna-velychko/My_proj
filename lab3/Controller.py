import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from View import *
from Model import *


def menu():
    flag = True
    engine = create_engine('postgres+psycopg2://postgres:6213@localhost:5432/firm')
    Session = sessionmaker(bind=engine)
    s = Session()
    flag = True
    while flag:
        print(" Enter:\n 1 - create\n 2 - delete \n 3 - edit\n 4 - get\n 5 - exit\n")
        item = int(input())
        if item == 5:
            flag = False
            continue
        if item == 1:
            (table, param1, param2) = menu_task1_create()
            create(s, table, param1, param2)
        elif item == 2:
            (table, param) = menu_task_1_delete()
            delete(s, table, param)
        elif item == 3:
            (table, param1, param2, param3) = menu_task_1_edit()
            edit(s, table, param1, param2, param3)
        elif item == 4:
            table = menu_task_1_print()
            print_table(s, table)
    s.close()


if __name__ == '__main__':
    menu()

