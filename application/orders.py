# table: food
from multiprocessing.connection import wait


def fetch_food_id(food_item):
    query = '''
    SELECT food_id
    FROM food_item
    WHERE food_name = '{name}'
    '''.format(name=food_item)
    return query

# table: contains
def add_contains(order_id, food_id):
    query = '''
    INSERT INTO contains VALUES ({oid}, {fid})
    '''.format(oid=order_id, fid=food_id)
    return query

# table: orders
def max_order_id():
    query = '''
    SELECT MAX(order_id)
    FROM orders
    '''
    return query

def add_order(order_id, customer_id, waiter_id):
    query = '''
    INSERT INTO orders VALUES({oid}, {cid}, {wid})
    '''.format(oid=str(int(order_id)+1), cid=customer_id, wid=waiter_id)
    return query

def fetch_total_price(oid):
    query = '''
    SELECT SUM(f.unit_price)
    FROM contains c
    LEFT JOIN food_item f
    ON c.food_id = f.food_id
    WHERE c.order_id = {}
    '''.format(oid)
    return query