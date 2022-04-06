def search_chef(id1):
    query = '''
    SELECT c.chef_id, c.first_name, c.last_name, c.phone_number
    FROM chef c
    WHERE c.chef_id = '{cid}'
    '''.format(cid=id1)
    return query


def search_order(id2):
    query = '''
    SELECT o.order_id,f.food_name,f.unit_price
    FROM chef c
    LEFT JOIN prepares p
    ON c.chef_id = p.chef_id
    LEFT JOIN orders o
    ON o.order_id = p.order_id
    LEFT JOIN contains n
    ON n.order_id = o.order_id
    LEFT JOIN food_item f
    ON f.food_id = n.food_id
    WHERE c.chef_id = '{cid}'
    '''.format(cid=id2)
    return query
