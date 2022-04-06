def search_menu(id1):
    query = '''
SELECT m.menu_id, m.menu_name, r.name, f.food_name, f.unit_price
FROM menu m
LEFT JOIN restaurant r
ON m.restaurant_id = r.restaurant_id
LEFT JOIN presents p
ON m.menu_id = p.menu_id
LEFT JOIN food_item f
ON f.food_id = p.food_id
WHERE m.menu_id = '{mid}'
    '''.format(mid=id1)
    return query

# table: orders
def max_food_id():
    query = '''
    SELECT MAX(food_id)
    FROM food_item
    '''
    return query

def add_item(fid, name,price):
    query = '''
           INSERT INTO food_item VALUES ({fid}, '{food_name}', {unit_price})
           '''.format(fid=fid+1,
                      food_name=name,
                      unit_price=price)
    return query


def add_present(mid, fid):
    query = '''
               INSERT INTO presents VALUES ({mid}, {fid})
               '''.format(mid=mid,
                          fid=fid)
    return query
