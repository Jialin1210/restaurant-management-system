

# Restaurant Management System

### Team Members

* Lynn Zhu - jz2969

* Carrol Song - js5989

### PostgreSQL Connection Settings

* User: jz2969
* Password: 6492
* DB-server: "35.211.155.104/proj1part2"

### Project Web Application URL

* URL of web application: http://34.148.150.249:8111/

### Description

We want to build a restaurant management system for restaurants and customers near Columbia University. Restaurant can better manage the menu and employees by keeping track of all orders, getting its employees' information, allocate the newly added order from customers to some waiters and chefs and complete these orders. Customer can see the list of restaurants in the customer page, choose one of them to see its menu, and add orders with their name, email address, and phone number. Waiter can see their personal information, the orders they took. Chef can see their personal information and the orders assigned to them.

#### Parts Implemented

[TODO: A description of the parts of your original proposal in Part 1 that you implemented, the parts you did not (which hopefully is nothing or something very small), and possibly new features that were not included in the proposal and that you implemented anyway. If you did not implement some part of the proposal in Part 1, explain why.]

* Home Page
  * connect every page mentioned below
  * make a summary about the number of restaurant, the number of customers, number of orders placed that used our system
* Restaurant Page
  * Show the list of restaurant name
  * Select a restaurant
    * show the menu with food item of the chosen restaurant
    * show the waiter and chef information as a query table

* Customer Page
  * Select a restaurant near Columbia University
    * Browse the menu with food item of the chosen restaurant
  * Place an order(s) by selecting food items from menu [insert values in `order` table, not `place` table]

* Chef Page
  * Search the chef
    * Query restaurant information
    * current orders assigned to them
  * [OPTIONAL] Update order status to ready once the order is prepared

* Waiter Page
  * Search the waiter
    * Query restaurant information
    * current orders assigned to them

* Menu Page
  * search menu for restaurant
  * Modify (add/drop) food item in the menu [in `present` table]

#### Parts Not Implemented

* All aspects shown in E/R diagram are covered.

### Interesting Pages

[TODO: Briefly describe two of the web pages that require (what you consider) the most interesting database operations in terms of what the pages are used for, how the page is related to the database operations (e.g., inputs on the page are used in such and such way to produce database operations that do such and such), and why you think they are interesting.]

* [TODO]
* Customer Page (Place an order): when the new customer place an order when he/she selects a restaurant, the order must be assigned to one of waiters in the chosen restaurant. So we randomly select the waiter from the restaurant and insert the order with customer information and waiter id.



### Appendix

Final E/R Diagram

![E_R Diagram](/Users/jialin/Downloads/E_R Diagram.png)