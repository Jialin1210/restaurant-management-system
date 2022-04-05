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