#!/usr/bin/env python

"""
Columbia's COMS W4111.003 Introduction to Databases
Author: Lynn Zhu

To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, abort, url_for
import application.restaurant, application.customer, application.orders
import application.waiter, application.chef, application.menu

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
conf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configuration')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@104.196.152.219/proj1part2
#
# For example, if you had username biliris and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://biliris:foobar@104.196.152.219/proj1part2"
#
with open(conf_dir + '/config.json') as f:
  config = json.load(f)
ip_address = '35.211.155.104'
DATABASEURI = "postgresql://" + config['user'] + ":" + config['password'] + "@" + ip_address + "/proj1part2"

#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
# engine.execute("""CREATE TABLE IF NOT EXISTS test (
#   id serial,
#   name text
# );""")
# engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")
# engine.execute("""DROP TABLE test""")

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print ("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/')
def home():
  res_cnt = g.conn.execute('''SELECT COUNT(DISTINCT name) FROM restaurant''')
  cus_cnt = g.conn.execute('''SELECT COUNT(customer_id) FROM customer''')
  order_cnt = g.conn.execute('''SELECT COUNT(order_id) FROM orders''')
  result = []
  for c in res_cnt:
    result.append(c)
  for c in cus_cnt:
    result.append(c)
  for c in order_cnt:
    result.append(c)
  return render_template('home.html', **dict(data = result))

@app.route('/restaurant/')
def restaurant():
  if request.method == 'GET':
    query = application.restaurant.fetch_all()
    cursor = g.conn.execute(query)
    result = []
    for c in cursor:
      result.append(c)
    return render_template('restaurant.html', **dict(res = result))
  return redirect("/")

@app.route('/search_restaurant/', methods=['POST'])
def search_restaurant():
  name = request.form['name']
  query = application.restaurant.fetch_menu(name)
  cursor = g.conn.execute(query)
  menu =[]
  for c in cursor:
    menu.append(c)
  
  query = application.restaurant.fetch_waiter(name)
  cursor = g.conn.execute(query)
  waiter_info = []
  for c in cursor:
    waiter_info.append(c)
  
  query = application.restaurant.fetch_chef(name)
  cursor = g.conn.execute(query)
  chef_info = []
  for c in cursor:
    chef_info.append(c)
  return render_template('restaurant_view.html', **dict(data1 = menu, data2 = waiter_info, data3 = chef_info))

@app.route('/customer/', methods=['GET', 'POST'])
def customer():
  if request.method == 'GET':
    query = application.restaurant.fetch_all()
    cursor = g.conn.execute(query)
    result = []
    for c in cursor:
      result.append(c)
    return render_template('customer.html', **dict(res = result))
  return redirect('/')

@app.route('/customer_menu/', methods=['POST'])
def customer_menu():
  name = request.form['name']
  query = application.restaurant.fetch_menu(name)
  cursor = g.conn.execute(query)
  menu =[]
  for c in cursor:
    menu.append(c)
  return render_template('customer_menu.html', **dict(data = menu))

@app.route('/add_order/', methods=['GET', 'POST'])
def add_order():
  if request.method == 'POST':
    query = application.orders.fetch_food_id(request.form['food_item']) # get food id
    cursor = g.conn.execute(query)
    food_id = 0
    for c in cursor:
      food_id = c
    food_id = food_id[0] # convert rowproxy to int
    
    total_price = 0
    if request.form.get('existing_order') is not None:
      order_id = request.form['order_id']
      query = application.orders.add_contains(order_id, food_id) # add food in existing order
      cursor = g.conn.execute(query)

      query = application.orders.fetch_total_price(order_id)
      cursor = g.conn.execute(query)
      for c in cursor:
        total_price = c
      total_price = total_price[0] # convert rowproxy to int
    else:
      query = application.customer.max_customer_id()
      cursor = g.conn.execute(query)
      customer_id = 0
      for c in cursor:
        customer_id = c
      customer_id = customer_id[0] # convert rowproxy to int
      query = application.customer.add_customer(customer_id, request.form) # insert new customer
      cursor = g.conn.execute(query)

      query = application.orders.max_order_id()
      cursor = g.conn.execute(query)
      order_id = 0
      for c in cursor:
        order_id = c
      order_id = order_id[0] # convert rowproxy to int

      query = application.waiter.fetch_waiter_id(request.form['restaurant'])
      cursor = g.conn.execute(query)
      waiter_id = 0
      for c in cursor:
        waiter_id = c
      waiter_id = waiter_id[0] # convert rowproxy to int
      query = application.orders.add_order(order_id, customer_id, waiter_id) # add new order
      cursor = g.conn.execute(query)

      order_id += 1 # update new order id
      query = application.orders.add_contains(order_id, food_id) # add food in existing order
      cursor = g.conn.execute(query)
      
      query = application.orders.fetch_total_price(order_id)
      cursor = g.conn.execute(query)
      for c in cursor:
        total_price = c
      total_price = total_price[0] # convert rowproxy to int
    return render_template('order_confirmation.html', oid=order_id, 
                            name=request.form['first_name'] + ' ' + request.form['last_name'],
                            price=total_price)

@app.route('/waiter/', methods=['GET','POST'])
def waiter():
  if "GET" == request.method:
    return render_template("waiters.html")
  else:
    id = request.form['waiter_id']
    query = application.waiter.search_waiter(id, request.form)
    cursor = g.conn.execute(query)
    waiter_info = []
    for c in cursor:
      waiter_info.append(c)
    query = application.waiter.search_order(id, request.form)
    cursor = g.conn.execute(query)
    order = []
    for c in cursor:
      order.append(c)
    return render_template('waiter.html', **dict(data1=waiter_info, data2=order))

@app.route('/assign_order/', methods=['GET','POST'])
def assign_order():
  if "POST" == request.method:
    cid = request.form['chef_id']
    oid = request.form['order_id']
    query = application.waiter.assign_order(cid, oid)
    cursor = g.conn.execute(query)
    return render_template("waiters.html")

@app.route('/chef/', methods=['GET','POST'])
def chef():
    if "GET" == request.method:
      return render_template("chefs.html")
    else:
        id = request.form['chef_id']
        query = application.chef.search_chef(id, request.form)
        cursor = g.conn.execute(query)
        chef_info = []
        for c in cursor:
          chef_info.append(c)
        query = application.chef.search_order(id, request.form)
        cursor = g.conn.execute(query)
        order = []
        for c in cursor:
          order.append(c)
        return render_template('chef.html', **dict(data1=chef_info, data2=order))

@app.route('/menu/', methods=['GET','POST'])
def menu():
  if "GET" == request.method:
    return render_template("menu.html")
  else:
    id = request.form['menu_id']
    query = application.menu.search_menu(id, request.form)
    cursor = g.conn.execute(query)
    menu_info = []
    for c in cursor:
      menu_info.append(c)
    return render_template('menu.html', **dict(data1=menu_info))
@app.route('/add_item/', methods=['GET','POST'])
def add_item():
  if "POST" == request.method:
    fid = request.form['food_id']
    mid = request.form['menu_id']
    query1 = application.menu.add_item(fid, request.form)
    query2 = application.menu.add_present(fid, mid)
    cursor1 = g.conn.execute(query1)
    cursor2 = g.conn.execute(query2)
    return render_template("menu.html")

'''
EXAMPLES
'''
#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/index/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  print (request.args)


  #
  # example of a database query
  #
  #cursor = g.conn.execute("SELECT name FROM tes
  #names = []
  #for result in cursor:
  #  names.append(result['name'])  # can also be accessed using result[0]
  #cursor.close()

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  context = dict(data = names)


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("index.html", **context)

#
# This is an example of a different path.  You can see it at:
# 
#     localhost:8111/another
#
# Notice that the function name is another() rather than index()
# The functions for each app.route need to have different names
#
@app.route('/another')
def another():
  return render_template("another.html")


# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  g.conn.execute('INSERT INTO test(name) VALUES (%s)', name)
  return redirect('/index')

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print ("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
