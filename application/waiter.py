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

def search_waiter(id, request):
    query = '''
SELECT
	w.waiter_id,
	w.first_name,
	w.last_name,
	w.phone_number
FROM
	waiter w
WHERE
	w.waiter_id = '{wid}'
AND w.first_name = '{first}'
AND w.last_name = '{last}'
AND w.phone_number = '{phone}'
    '''.format(wid=id,
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
FROM waiter w
LEFT JOIN takes t
ON w.waiter_id = t.waiter_id
LEFT JOIN order o
ON o.order_id = t.order_id
WHERE
	w.waiter_id = '{wid}'
AND w.first_name = '{first}'
AND w.last_name = '{last}'
AND w.phone_number = '{phone}'
    '''.format(wid=id,
    first=request['first_name'],
    last=request['last_name'],
    phone=request['phone_number'])
    return query
def assign_order(cid, oid):
    query = '''
       INSERT INTO prepares VALUES ({cid}, {oid})
       '''.format(cid=str(int(cid)),
                  oid=str(int(oid)))
    return query