def max_customer_id():
    query = '''
    SELECT MAX(customer_id)
    FROM customer
    '''
    return query

def add_customer(id, request):
    query = '''
    INSERT INTO customer VALUES ({cid}, '{first}', '{last}', '{email}', '{phone}')
    '''.format(cid=str(int(id)+1), 
    first=request['first_name'], 
    last=request['last_name'], 
    email=request['email_address'],
    phone=request['phone_number'])
    return query