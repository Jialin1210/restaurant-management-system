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