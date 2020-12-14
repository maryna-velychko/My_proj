def menu_task1_create():
    print(" Choose table:\n Costumer - press 1\n Firm - press 2\n Product - press 3\n Costumer_Product - press 4\n Firm_Product - press 5")
    table = int(input())
    param1 = None
    param2 = None
    if table == 1:
        print("Enter costumer name\n")
        param1 = input()
        print("Enter costumer e-mail\n")
        param2 = input()
    elif table == 2:
        print("Enter firm name\n")
        param1 = input()
        print("Enter firm address\n")
        param2 = input()
    elif table == 3:
        print("Enter product name\n")
        param1 = input()
        print("Enter prise product\n")
        param2 = float(input())
    elif table == 4:
        print("Enter costumer id\n")
        param1 = int(input())
        print("Enter article product\n")
        param2 = int(input())
    elif table == 5:
        print("Enter firm name\n")
        param1 = input()
        print("Enter article product\n")
        param2 = int(input())
    else:
        print("False number")
        return
    return table, param1, param2


def menu_task_1_delete():
    print(" Choose table:\n Costumer - press 1\n Firm - press 2\n Product - press 3\n Costumer_Product - press 4\n Firm_Product - press 5")
    table = int(input())
    if table == 1:
        print("Enter the id of the client you want to delete\n")
    elif table == 2:
        print("Enter the name of the firm you want to delete\n")
    elif table == 3 or table == 4 or table == 5:
        print("Enter the article of the product you want to delete\n")
    else:
        print("False number")
        return
    parameter = input()
    return table, parameter


def menu_task_1_edit():
    print(" Choose table:\n Costumer - press 1\n Firm - press 2\n Product - press 3\n Costumer_Product - press 4\n Firm_Product - press 5")
    table = int(input())
    (param1, param2, param3) = (None, None, None)
    if table == 1:
        print("Enter costumer name\n")
        param1 = input()
        print("Enter costumer e-mail\n")
        param2 = input()
        print("Enter the id of the client you want to edit\n")
        param3 = int(input())
    elif table == 2:
        print("Enter firm name\n")
        param1 = input()
        print("Enter firm address\n")
        param2 = input()
        print("Enter the name of the firm you want to edit\n")
        param3 = input()
    elif table == 3:
        print("Enter product name\n")
        param1 = input()
        print("Enter prise product\n")
        param2 = float(input())
        print("Enter the article of the product you want to edit\n")
        param3 = int(input())
    elif table == 4:
        print("Enter costumer id\n")
        param1 = int(input())
        print("Enter article product\n")
        param2 = int(input())
        print("Enter the article of the product you want to edit\n")
        param3 = int(input())
    elif table == 5:
        print("Enter firm name\n")
        param1 = input()
        print("Enter article product\n")
        param2 = int(input())
        print("Enter the article of the product you want to edit\n")
        param3 = int(input())
    else:
        print("False number")
        return
    return table, param1, param2, param3


def menu_task_1_print():
    print(" Choose table:\n Costumer - press 1\n Firm - press 2\n Product - press 3\n Costumer_Product - press 4\n Firm_Product - press 5")
    table = int(input())
    return table
