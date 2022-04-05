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