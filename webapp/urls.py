from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/index', views.rest_index, name='rest_index'),

    path('register/customer/', views.customer_register, name='customer_register'),
    path('register/customer/profile', views.customer_profile_register, name='customer_profile_register'),
    path('login/customer/', views.customer_login, name='customer_login'),
    path('login/restaurant/', views.restaurant_login, name='restaurant_login'),
    path('register/restaurant/', views.restaurant_register, name='restaurant_register'),
    path('register/restaurant/profile', views.restaurant_profile_register, name='restaurant_profile_register'),
    path('restaurant/detail', views.restaurant_detail, name='restaurant_detail'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('restaurants/', views.restaurant_index, name='restaurant_index'),
    path('myorders/', views.myorders, name='myorders'),

    path('orderplaced/', views.orderplaced),
    # path('restaurant/',views.restuarent,name='restuarant'),
    path('restaurant/profile', views.restaurantProfile, name='rest_profile'),
    path('restaurant/menu/', views.menu_manipulation, name='menu'),
    # url(r'ajax/favourite_ajax/$', views.favorite_ajax, name='favorite_ajax'),
    # url: "/home/favoriteAjax/",
    # url(r'ajax/entity_name/$', EntityAjaxView.as_view(), name='entity_name'),

    # path('profile/user/',views.customerProfile,name='profile'),
    # path('user/create/',views.createCustomer,name='ccreate'),
    # path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    # path('restaurant/create/',views.createRestaurant,name='rcreate'),
    # path('restaurant/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('restaurant/orderlist/', views.orderlist, name='orderlist'),
    # path('restaurant/menu/',views.menuManipulation,name='mmenu'),
    path('restaurant/<int:pk>/', views.restuarantMenu, name='menu'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/pay', views.pay, name='pay'),

]
