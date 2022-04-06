def fetch_waiter_id(restaurant):
    query = '''
    SELECT w.waiter_id
    FROM restaurant r 
    LEFT JOIN waiter w
    ON r.restaurant_id = w.restaurant_id
    WHERE r.name = '{}'
    ORDER BY RANDOM()
    LIMIT 1
    '''.format(restaurant)
    return query


def search_waiter(id1):
    query = '''
SELECT w.waiter_id, w.first_name, w.last_name, w.phone_number
FROM waiter w
WHERE w.waiter_id = '{wid}'
    '''.format(wid=id1)
    return query


def search_order(id2):
    query = '''
    SELECT o.order_id,f.food_name,f.unit_price
    FROM waiter w
    LEFT JOIN orders o
    ON w.waiter_id = o.waiter_id
    LEFT JOIN contains c
    ON c.order_id = o.order_id
    LEFT JOIN food_item f
    ON f.food_id = c.food_id
    WHERE w.waiter_id = '{wid}'
        '''.format(wid=id2)
    return query


def assign_order(cid, wid):
    query = '''
      insert into tells values ({wid}, {cid})
       '''.format(wid=str(int(wid)), cid=str(int(cid)))
    return query


def find_chef():
    query = '''select chef_id from chef order by RANDOM() LIMIT 1'''
    return query


def find_waiter(oid):
    query = ''' select waiter_id from orders where order_id = '{oid}' '''.format(oid=str(int(oid)))
    return query