from django.contrib import admin
from .models import Customer, User, Restaurant, RestaurantOwner, FoodItem, FoodRestaurant, Offer, Order, OrderDetail, \
    Favourite, Location, ItemType, Payment, Cuisine

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(RestaurantOwner)
admin.site.register(ItemType)
admin.site.register(FoodRestaurant)
admin.site.register(FoodItem)
admin.site.register(OrderDetail)
admin.site.register(Order)
admin.site.register(Offer)
admin.site.register(Favourite)
admin.site.register(Location)
admin.site.register(Cuisine)
admin.site.register(Payment)
