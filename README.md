

# Restaurant Management System

### Team Members

* Lynn Zhu - jz2969

* Carrol Song - js5989

### PostgreSQL Connection Settings

* User: jz2969
* Password: 6492
* DB-server: "35.211.155.104/proj1part2"

### Project Web Application URL

* URL of web application: http://34.75.86.29:8111/

### Description

We want to build a restaurant management system for restaurants and customers near Columbia University. Restaurants can better manage the menu and employees by updating menus (add more food items in menu), extracting its employees' information, assign the newly added order from customers to some waiters and chefs and complete these orders. Customers can see the list of restaurants in the customer page, choose one of them to see its menu, and place an order with their name, email address, and phone number. Waiters can see their personal information and the orders they took, and they can also assign new orders to chef in the same restaurant. Chef can see their personal information and the orders assigned to them and prepare for food.

#### Parts Implemented

* Home Page: This page makes a brief summary about the impact of our restaurant management system. It lists the number of restaurant, the number of customers, number of orders placed using our system and the contributors' name.
* Restaurant Page: This page is designed for restaurant owners who would like to see the menu and employee information. It shows the whole list of restaurant names. We allow the page to search over the restaurant names and it displays the menu with food item of the chosen restaurant, waiter information, and chef information.
* Customer Page: This page is designed for customers who would like to browse the menu and place an order. The page lists the whole list of restaurant names, and it allows customers to search over the names to see the menu with food item. The page also allows customers to create an order by either adding food from menu to the existing order, or creating a new order. After submission, the customer will see a confirmation page that contains the Order ID, customer's name, and the total price for the order.
* Waiter Page: This page is designed for waiters to input their ID and have a look at the orders assigned to them. The orders will also come with the food item and the unit price.
* Chef Page: This page is designed for chefs to input their ID and to see the orders they need to prepare for, which achieves the relationship between `chef` and `orders` (i.e., `prepares` shown in ER diagram).
* Menu Page: This page is designed for restaurant to search their menu and modify it by adding new food items.

#### Parts Not Implemented

* All aspects shown in ER diagram/described in proposal in part 1 are covered.

### Interesting Pages

* Customer Page (Place an order): The page contains lots of SQL queries, such as `customer`, `orders`, `contains`, because we consider about two scenarios about placing the order. The first one is when the customer already shown in `customer` table would like to add more food on the existing order, and the other one is to create an order with a new Order ID. For the first scenario, we didn't insert customer information in database, and we instead find the order with the existing Order ID. As for the second scenario, we not only create customer information, but also create a new order in `order` table. In addition, the order must be assigned to one of waiters in the chosen restaurant. So we randomly select the waiter from the restaurant and insert the order with customer information and waiter id.

* Menu Page (add a food item): This page contains lots of SQL queries, because of the `menu`--`presents`--`food_item` relationship. Therefore, we need to not only create a new item in `food_item` table, but also make the connection between menu ID and food ID through `presents` so that we can see the updated menu after we refresh the page.

### Appendix

Final E/R Diagram

![E_R Diagram](https://github.com/Jialin1210/restaurant-management-system/blob/master/E_R%20Diagram.png)
