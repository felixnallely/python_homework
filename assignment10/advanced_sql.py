import sqlite3

#Task 1: Complex JOINs with Aggregation

def task1(cursor):
    query = """
        SELECT 
            orders.order_id,
            SUM(line_items.quantity * products.price) AS total_price
        FROM orders 
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id 
        LIMIT 5;
    """
    cursor.execute(query)

    print("\nFirst 5 orders with total price:")
    for row in cursor.fetchall():
        print(row)


#Task 2: Understanding Subqueries 
##Creating an inner query 
def task2(cursor):
    query = """
        SELECT
            customers.customer_name, 
            AVG(sub.total_price) AS average_total_price
        FROM customers 
        LEFT JOIN (
            SELECT
                orders.customer_id AS customer_id_b,
                SUM(line_items.quantity * products.price) AS total_price
            FROM orders
            JOIN line_items ON orders.order_id = line_items.order_id
            JOIN products ON line_items.product_id = products.product_id
            GROUP BY orders.order_id
        ) AS sub
        ON customers.customer_id = sub.customer_id_b
        GROUP BY customers.customer_id;
    """

    cursor.execute(query)

    print("\nAverage order price per customer:")
    for row in cursor.fetchall():
        print(row)

#Task 3: An Insert Transaction Based on Data 
#customer: customer_id, customer_name
#employee: employee_id, first_name, last_name, phone
#products: product_id, product_name, price 
#orders: order_id, customer_id, employee_id, date
#line_items: line-item_id, order_id, product_id, quantity

def task3(cursor, conn):
    conn.execute("PRAGMA foreign_keys = 1")

    #customer_id for Perez and Sons
    cursor.execute("""
        SELECT customer_id
        FROM customers
        WHERE customer_name = 'Perez and Sons';
    """)
    customer_id = cursor.fetchone()[0]

    #employee_id for Miranda Harris 
    cursor.execute("""
        SELECT employee_id
        FROM employees
        WHERE first_name = 'Miranda' AND last_name = 'Harris';
    """)
    employee_id = cursor.fetchone()[0]

    #products_id for least expensive 5 products 
    cursor.execute("""
        SELECT product_id
        FROM products
        ORDER BY price ASC
        LIMIT 5;
    """)
    product_ids = [row[0] for row in cursor.fetchall()]

    conn.execute("BEGIN")

    #new order/ get order_id
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, DATE('now'))
        RETURNING order_id;
    """, (customer_id, employee_id))

    order_id = cursor.fetchone()[0]

    #line_items (5)
    for pid in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, 10);
        """, (order_id, pid))

    conn.commit()

    #print order 
    cursor.execute("""
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            products.product_name
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?;
    """, (order_id,))

    print("\nLine items for new order:")
    for row in cursor.fetchall():
        print(row)

#Task 4: 
def task4(cursor):
    query = """
        SELECT
            employees.employee_id,
            employees.first_name,
            employees.last_name,
            COUNT(orders.order_id) AS order_count
        FROM employees
        JOIN orders ON employees.employee_id = orders.employee_id
        GROUP BY employees.employee_id
        HAVING COUNT(orders.order_id) > 5;
    """

    cursor.execute(query)

    print("\nEmployees that have more than 5 orders:")
    for row in cursor.fetchall():
        employee_id, first_name, last_name, order_count = row
        print(employee_id, first_name, last_name, order_count)


#the main so tasks can run 
def main():
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    task1(cursor)
    task2(cursor)
    task3(cursor, conn)
    task4(cursor)

    conn.close()
main()