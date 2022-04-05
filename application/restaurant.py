def fetch_all():
    query = '''SELECT * FROM restaurant'''
    return query

def fetch_menu(name):
    query = '''
    SELECT r.name, m.menu_name, f.food_name, f.unit_price 
    FROM restaurant r 
    LEFT JOIN menu m 
    ON r.restaurant_id = m.restaurant_id 
    LEFT JOIN presents p 
    ON p.menu_id = m.menu_id 
    LEFT JOIN food_item f 
    ON f.food_id = p.food_id 
    WHERE r.name = '{}'
    ORDER BY m.menu_name DESC
    '''.format(name)
    return query

def fetch_waiter(name):
    query = '''
    SELECT r.name, CONCAT(w.first_name, ' ', w.last_name) as waiter_name, w.phone_number 
    FROM restaurant r 
    LEFT JOIN waiter w
    ON r.restaurant_id = w.restaurant_id
    WHERE r.name = '{}'
    '''.format(name)
    return query

def fetch_chef(name):
    query = '''
    SELECT r.name, CONCAT(c.first_name, ' ', c.last_name) as chef_name, c.phone_number
    FROM restaurant r
    LEFT JOIN waiter w
    ON r.restaurant_id = w.restaurant_id
    LEFT JOIN tells t
    ON w.waiter_id = t.waiter_id
    LEFT JOIN chef c
    ON c.chef_id = t.chef_id
    WHERE r.name = '{}'
    '''.format(name)
    return query