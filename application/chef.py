import logging
from sqlalchemy import text


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
    '''.format(cid=str(int(id)),
    first=request['first_name'],
    last=request['last_name'],
    phone=request['phone_number'])
    return query