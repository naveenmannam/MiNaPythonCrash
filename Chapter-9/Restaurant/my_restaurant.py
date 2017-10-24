from restaurant import Restaurant, Icecream

restaurant_1 = Restaurant("Michnaro", "Chinese")
restaurant_1.describe_restaurant()
restaurant_1.set_customer_served(23)
restaurant_1.customers_served()
restaurant_1.increment_customers(34)
restaurant_1.customers_served()
print()

restaurant_2 = Icecream("Sandy", "Indian")
restaurant_2.describe_restaurant()
restaurant_2.set_customer_served(23)
restaurant_2.customers_served()
restaurant_2.display_flavors()
