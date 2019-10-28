from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/customer/', views.customer_register, name='customer_register'),
    path('register/customer/profile', views.customer_profile_register, name='customer_profile_register'),
    path('login/customer/', views.customer_login, name='customer_login'),
    path('login/restaurant/', views.restaurant_login, name='restaurant_login'),
    path('register/restaurant/', views.restaurant_register, name='restaurant_register'),
    path('register/restaurant/profile', views.restaurant_profile_register, name='restaurant_profile_register'),
    path('restaurant/detail', views.restaurant_detail, name='restaurant_detail'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('restaurants/', views.restaurant_index, name='restaurant_index'),

    # path('orderplaced/',views.orderplaced),
    # path('restaurant/',views.restuarent,name='restuarant'),
    path('restaurant/profile', views.restaurantProfile, name='rest_profile'),
    path('restaurant/menu/', views.menu_manipulation, name='menu'),

    # path('profile/user/',views.customerProfile,name='profile'),
    # path('user/create/',views.createCustomer,name='ccreate'),
    # path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    # path('restaurant/create/',views.createRestaurant,name='rcreate'),
    # path('restaurant/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('restaurant/orderlist/', views.orderlist, name='orderlist'),
    # path('restaurant/menu/',views.menuManipulation,name='mmenu'),
    path('restaurant/<int:pk>/', views.restuarantMenu, name='menu'),
    path('checkout/', views.checkout, name='checkout'),

]
