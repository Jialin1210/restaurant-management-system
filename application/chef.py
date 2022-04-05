def search_chef(id, request):
    query = '''
SELECT
	c.chef_id,
	c.first_name,
	c.last_name,
	c.phone_number
FROM
	chef c
WHERE
	c.chef_id = '{cid}'
AND c.first_name = '{first}'
AND c.last_name = '{last}'
AND c.phone_number = '{phone}'
    '''.format(cid=id,
               first=request['first_name'],
               last=request['last_name'],
               phone=request['phone_number'])
    return query


def search_order(id, request):
    query = '''
SELECT
	o.order_id,
	o.num_of_items,
    o.total_price
FROM chef c
LEFT JOIN prepares p
ON c.chef_id = p.chef_id
LEFT JOIN order o
ON o.order_id = p.order_id
WHERE
	c.chef_id = '{cid}'
AND c.first_name = '{first}'
AND c.last_name = '{last}'
AND c.phone_number = '{phone}'
    '''.format(cid=id,
               first=request['first_name'],
               last=request['last_name'],
               phone=request['phone_number'])
    return query
