def search_menu(id, request):
    query = '''
SELECT
	m.menu_id,
	m.price
FROM
	menu m
WHERE
	m.menu_id = '{mid}'
AND m.price = '{price}'
    '''.format(mid=str(int(id)),
    price=request['price'])
    return query
def add_item(id, request):
    query = '''
           INSERT INTO food_item VALUES ({fid}, '{food_name}', '{unit_price}')
           '''.format(fid=str(int(id)+1),
                      unit_price=request['unit_price'])
    return query
def add_present(fid, mid):
    query = '''
               INSERT INTO food_item VALUES ({fid}, {mid})
               '''.format(fid=str(int(fid)),
                          mid=str(int(mid)))
    return query