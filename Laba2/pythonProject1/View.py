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
    print(" Enter name table:\n costumer \n firm \n product \n costumer_product\n firm_product")
    table = input()
    return table


def menu_task_2():
    print(" Choose table:\n Costumer - press 1\n Firm - press 2\nProduct - press 3\n Costumer_Product - press 4\n Firm_Product - press 5")
    table = int(input())
    if table == 1 or table == 2 or table == 3:
        print(" Input number of lines in tables")
    else:
        print(" Enter the percentage of the total number of records in the two tables (0 < number <= 100)")
    number = int(input())
    return table, number


def menu_task_3():
    print(" Enter: 1, 2 or 3 for testing select")
    item_3 = int(input())
    if item_3 == 1:
        print("Enter the product article to display the name of the customer who bought it")
    elif item_3 == 2:
        print("Enter the product article to display the address of the firm who produces it")
    elif item_3 == 3:
        print("Enter the customer ID to find out the total cost of his purchases")
    else:
        print("False number")
        return
    param = input()
    return param, item_3
