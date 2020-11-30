import psycopg2
import time
from psycopg2 import errors


def create(cursor, table, parameter_1, parameter_2):
    try:
        if table == 1:
            cursor.execute("INSERT INTO costumer (name_costumer, email) VALUES (%s, %s)", (parameter_1, parameter_2))
        elif table == 2:
            cursor.execute("INSERT INTO firm (name_firm, address) VALUES (%s, %s)", (parameter_1, parameter_2))
        elif table == 3:
            cursor.execute("INSERT INTO product (name_product, price) VALUES (%s, %s)", (parameter_1, float(parameter_2)))
        elif table == 4:
            cursor.execute("INSERT INTO costumer_product (id, article) VALUES (%s, %s)", ([parameter_1], [parameter_2]))
        elif table == 5:
            cursor.execute("INSERT INTO firm_product (name_firm, article) VALUES (%s, %s)", (parameter_1, [parameter_2]))
    except errors.ForeignKeyViolation:
        print("Error, ENTER WRONG DATA\n")


def delete(cursor, table, parameter):
    if table == 1:
        cursor.execute("DELETE FROM costumer WHERE id = %s", [parameter])
    elif table == 2:
        cursor.execute("DELETE FROM firm WHERE name_firm = %s", parameter)
    elif table == 3:
        cursor.execute("DELETE FROM product WHERE article = %s", [parameter])
    elif table == 4:
        cursor.execute("DELETE FROM costumer_product WHERE article = %s", [parameter])
    elif table == 5:
        cursor.execute("DELETE FROM firm_product WHERE article = %s", [parameter])


def edit(cursor, table, parameter_1, parameter_2, parameter_3):
    try:
        if table == 1:
            cursor.execute("UPDATE costumer SET name_costumer = %s, email = %s WHERE id = %s", (parameter_1, parameter_2, [parameter_3],))
        elif table == 2:
            cursor.execute("UPDATE firm SET name_firm = %s, address = %s WHERE name_firm = %s", (parameter_1, parameter_2, parameter_3,))
        elif table == 3:
            cursor.execute("UPDATE product SET name_product = %s, price = %s WHERE article = %s", (parameter_1, float(parameter_2), parameter_3,))
        elif table == 4:
            cursor.execute("UPDATE costumer_product SET article = %s, id = %s WHERE article = %s", (parameter_1, parameter_2, parameter_3,))
        elif table == 5:
            cursor.execute("UPDATE firm_product SET name_firm = %s, article = %s WHERE article = %s", (parameter_1, parameter_2, parameter_3,))
    except errors.ForeignKeyViolation:
        print("Error, ENTER WRONG DATA\n")


def print_table(cursor, table):
    cursor.execute("SELECT * FROM {}".format(table))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def random_generation(cursor, table, number):
    try:
        if table == 1:
            cursor.execute("INSERT INTO costumer (name_costumer, email) "
                           " SELECT chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int),"
                           " chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int)"
                           " FROM generate_series(1, %s)", [number])
        elif table == 2:
            cursor.execute("INSERT INTO firm (name_firm, address) "
                           " SELECT chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int),"
                           " chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int)"
                           " FROM generate_series(1, %s)", [number])
        elif table == 2:
            cursor.execute("INSERT INTO firm (name_firm, address) "
                           " SELECT chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int),"
                           " chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int)"
                           " FROM generate_series(1, %s)", [number])
        elif table == 3:
            cursor.execute("INSERT INTO product (name_product, price) "
                           " SELECT chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int),"
                           " trunc(random()*100 + random())::real FROM generate_series(1, %s)",
                           [number])
        elif table == 4:
            cursor.execute("INSERT INTO costumer_product (article, id) SELECT article, id FROM product TABLESAMPLE"
                           " bernoulli(%s), costumer TABLESAMPLE bernoulli(%s)", (number, number,))
        elif table == 5:
            cursor.execute("INSERT INTO firm_product (name_firm, article) SELECT name_firm, article"
                           " FROM firm TABLESAMPLE"
                           " bernoulli(%s), costumer TABLESAMPLE bernoulli(%s)", (number, number,))
    except psycopg2.errors.UniqueViolation:
        print("Error\n")


def select_function(cursor, parameter, item):
        if item == 1:
            t1 = time.perf_counter()
            cursor.execute("with table_1 as (SELECT id FROM costumer_product"
                           " where costumer_product.article = %s)"
                           " SELECT name_costumer FROM costumer inner join table_1 on costumer.id = table_1.id",
                           [parameter])
            t2 = time.perf_counter()
            row = cursor.fetchone()
            print("Name costumer")
            print(row)
            print("Request processing time ", t2 - t1)
        elif item == 2:
            t1 = time.perf_counter()
            cursor.execute("with table_1 as (SELECT name_firm FROM firm_product"
                           " where firm_product.article = %s)"
                           " SELECT address FROM firm inner join table_1 on firm.name_firm = table_1.name_firm",
                           [parameter])
            t2 = time.perf_counter()
            row = cursor.fetchone()
            print("Firm Address")
            print(row)
            print("Request processing time ", t2 - t1)
        elif item == 3:
            t1 = time.perf_counter()
            cursor.execute("with table_1 as (SELECT article FROM costumer_product"
                           " where costumer_product.id = %s)"
                           " SELECT sum(price) FROM product inner join table_1 on product.article = table_1.article",
                           [parameter])
            t2 = time.perf_counter()
            row = cursor.fetchone()
            print("Price")
            print(row)
            print("Request processing time ", t2 - t1)
