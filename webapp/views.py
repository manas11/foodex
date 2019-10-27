from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from xdg import Menu

from webapp.models import Location, RestaurantOwner, Restaurant, FoodRestaurant, FoodItem, ItemType
from .forms import CustomerRegisterForm, CustomerRegisterProfileForm, RestaurantRegisterForm, \
    RestaurantRegisterProfileForm, RestaurantDetailForm


# from django.contrib.auth.decorators import login_required
# from collections import Counter
# from django.urls import reverse
# from django.db.models import Q
#
#
# # from .models import Customer, Restaurant, Item, Menu, Order, orderItem, User
#
#
# #### ---------- General Side -------------------#####
#
# Showing index page


def index(request):
    return render(request, 'webapp/index.html', {})


def logout_view(request):
    logout(request)
    return redirect("index")


def customer_register(request):
    form = CustomerRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.is_customer = True
        user.set_password(password)
        user.save()
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('customer_profile_register')
    context = {
        'form': form
    }
    return render(request, 'webapp/customer_register.html', context)


def customer_profile_register(request):
    form = CustomerRegisterProfileForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        # print(instance)
        instance.location_id = 1
        instance.save()
        return redirect("index")
    context = {
        'form': form,
        'title': "Complete Your profile"
    }
    return render(request, 'webapp/customer_profile_register.html', context)


def customer_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass']
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'webapp/customer_login.html', {'error_message': 'Your account disable'})
    else:
        return render(request, 'webapp/customer_login.html', {'error_message': 'Your account disable'})


def restaurant_register(request):
    form = RestaurantRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.is_restaurant_owner = True
        user.set_password(password)
        user.save()
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('restaurant_profile_register')
    context = {
        'form': form
    }
    return render(request, 'webapp/restaurant_register.html', context)


def restaurant_profile_register(request):
    form = RestaurantRegisterProfileForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        # print(instance)
        instance.location_id = 1
        instance.save()
        return redirect("restaurant_detail")
    context = {
        'form': form,
        'title': "Complete Your profile"
    }
    return render(request, 'webapp/restaurant_profile_register.html', context)


def restaurant_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass']
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'webapp/restaurant_login.html', {'error_message': 'Your account disable'})
    else:
        return render(request, 'webapp/restaurant_login.html', {'error_message': 'Your account disable'})


def restaurant_detail(request):
    form = RestaurantDetailForm(request.POST or None, request.FILES or None)
    print("qe")
    if form.is_valid():
        instance = form.save(commit=False)
        print("e")
        restaurantowner = RestaurantOwner.objects.get(user_id=request.user.id)
        instance.owner = restaurantowner
        # print(restaurantowner)
        instance.location_id = 1
        instance.offer_id = 1
        instance.cuisine_id = 1
        instance.save()
        return redirect("index")
    context = {
        'form': form,
        'title': "Complete Your profile"
    }
    return render(request, 'webapp/restaurant_detail.html', context)


def restaurant_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'webapp/restaurant_index.html', {'restaurants': restaurants})


# def orderplaced(request):

# #     return render(request, 'webapp/orderplaced.html', {})
# #
# #
# # # Showing Restaurants list to Customer
# # def restuarent(request):
# #     r_object = Restaurant.objects.all()
# #     query = request.GET.get('q')
# #     if query:
# #         r_object = Restaurant.objects.filter(Q(rname__iins=query)).distinct()
# #         return render(request, 'webapp/restaurents.html', {'r_object': r_object})
# #     return render(request, 'webapp/restaurents.html', {'r_object': r_object})
# #
# #
# logout


# # # customer profile view
# # def customerProfile(request, pk=None):
# #     if pk:
# #         user = User.objects.get(pk=pk)
# #     else:
# #         user = request.user
# #
# #     return render(request, 'webapp/profile.html', {'user': user})
# #
# #
#
# #
# # #  Update customer detail
# # def updateCustomer(request, id):
# #     form = CustomerForm(request.POST or None, instance=request.user.customer)
# #     if form.is_valid():
# #         form.save()
# #         return redirect('profile')
# #     context = {
# #         'form': form,
# #         'title': "Update Your profile"
# #     }
# #     return render(request, 'webapp/customer_profile_register.html', context)
# #
# #
# # def restuarantMenu(request, pk=None):
# #     menu = Menu.objects.filter(r_id=pk)
# #     rest = Restaurant.objects.filter(id=pk)
# #
# #     items = []
# #     for i in menu:
# #         item = Item.objects.filter(fname=i.item_id)
# #         for content in item:
# #             temp = []
# #             temp.append(content.fname)
# #             temp.append(content.category)
# #             temp.append(i.price)
# #             temp.append(i.id)
# #             temp.append(rest[0].status)
# #             temp.append(i.quantity)
# #             items.append(temp)
# #     context = {
# #         'items': items,
# #         'rid': pk,
# #         'rname': rest[0].rname,
# #         'rmin': rest[0].min_ord,
# #         'rinfo': rest[0].info,
# #         'rlocation': rest[0].location,
# #     }
# #     return render(request, 'webapp/menu.html', context)
# #
# #
# # @login_required(login_url='/login/user/')
# # def checkout(request):
# #     if request.POST:
# #         addr = request.POST['address']
# #         ordid = request.POST['oid']
# #         Order.objects.filter(id=int(ordid)).update(delivery_addr=addr,
# #                                                    status=Order.ORDER_STATE_PLACED)
# #         return redirect('/orderplaced/')
# #     else:
# #         cart = request.COOKIES['cart'].split(",")
# #         cart = dict(Counter(cart))
# #         items = []
# #         totalprice = 0
# #         uid = User.objects.filter(username=request.user)
# #         oid = Order()
# #         oid.orderedBy = uid[0]
# #         for x, y in cart.items():
# #             item = []
# #             it = Menu.objects.filter(id=int(x))
# #             if len(it):
# #                 oiid = orderItem()
# #                 oiid.item_id = it[0]
# #                 oiid.quantity = int(y)
# #                 oid.r_id = it[0].r_id
# #                 oid.save()
# #                 oiid.ord_id = oid
# #                 oiid.save()
# #                 totalprice += int(y) * it[0].price
# #                 item.append(it[0].item_id.fname)
# #                 it[0].quantity = it[0].quantity - y
# #                 it[0].save()
# #                 item.append(y)
# #                 item.append(it[0].price * int(y))
# #
# #             items.append(item)
# #         oid.total_amount = totalprice
# #         oid.save()
# #         context = {
# #             "items": items,
# #             "totalprice": totalprice,
# #             "oid": oid.id
# #         }
# #         return render(request, 'webapp/order.html', context)
# #
# #
# # ####### ------------------- Restaurant Side ------------------- #####
# #
# # # creating restuarant account
# # def restRegister(request):
# #     form = RestuarantSignUpForm(request.POST or None)
# #     if form.is_valid():
# #         user = form.save(commit=False)
# #         username = form.cleaned_data['username']
# #         password = form.cleaned_data['password']
# #         user.is_restaurant = True
# #         user.set_password(password)
# #         user.save()
# #         user = authenticate(username=username, password=password)
# #         if user is not None:
# #             if user.is_active:
# #                 login(request, user)
# #                 return redirect("rcreate")
# #     context = {
# #         'form': form
# #     }
# #     return render(request, 'webapp/restsignup.html', context)
# #
# #
# # # restuarant login
# # def restLogin(request):
# #     if request.method == "POST":
# #         username = request.POST['username']
# #         password = request.POST['password']
# #         user = authenticate(username=username, password=password)
# #         if user is not None:
# #             if user.is_active:
# #                 login(request, user)
# #                 return redirect("rprofile")
# #             else:
# #                 return render(request, 'webapp/restlogin.html', {'error_message': 'Your account disable'})
# #         else:
# #             return render(request, 'webapp/restlogin.html', {'error_message': 'Invalid Login'})
# #     return render(request, 'webapp/restlogin.html')
# #
# #
# # # restaurant profile view
# # def restaurantProfile(request, pk=None):
# #     if pk:
# #         user = User.objects.get(pk=pk)
# #     else:
# #         user = request.user
# #
# #     return render(request, 'webapp/rest_profile.html', {'user': user})
# #
# #
# # # create restaurant detail
# # @login_required(login_url='/login/restaurant/')
# # def createRestaurant(request):
# #     form = RestuarantForm(request.POST or None, request.FILES or None)
# #     if form.is_valid():
# #         instance = form.save(commit=False)
# #         instance.user = request.user
# #         instance.save()
# #         return redirect("rprofile")
# #     context = {
# #         'form': form,
# #         'title': "Complete Your Restaurant profile"
# #     }
# #     return render(request, 'webapp/rest_profile_form.html', context)
# #
# #
# # # Update restaurant detail
# # @login_required(login_url='/login/restaurant/')
# # def updateRestaurant(request, id):
# #     form = RestuarantForm(request.POST or None, request.FILES or None, instance=request.user.restaurant)
# #     if form.is_valid():
# #         form.save()
# #         return redirect('rprofile')
# #     context = {
# #         'form': form,
# #         'title': "Update Your Restaurant profile"
# #     }
# #     return render(request, 'webapp/rest_profile_form.html', context)
# #
# #
# add  menu item for restaurant
@login_required(login_url='/login/restaurant/')
def menu_manipulation(request):
    if not request.user.is_authenticated:
        return redirect("rlogin")
    rest = Restaurant.objects.get(owner=RestaurantOwner.objects.get(user_id=request.user.id))
    if request.POST:
        print("8")
        rtype = request.POST['submit']
        print(rtype)
        if rtype == "Modify":
            print("23")
            foodid = int(request.POST['fooditemid'])
            food = FoodRestaurant.objects.get(food_item_id=foodid)
            food.cost = int(request.POST['cost'])
            foodItem = FoodItem.objects.get(food_item_id=foodid)
            foodItem.name = request.POST['name']
            is_veg = request.POST['is_veg']
            print(is_veg)
            if is_veg:
                foodItem.is_veg = True
            else:
                foodItem.is_veg = False

            ittype = ItemType.objects.get(type_id=request.POST['type'])
            foodItem.type = ittype
            foodItem.save()
            food.save()

        elif rtype == "Add":
            print("13")
            foodrest = FoodRestaurant()
            name = request.POST['name']
            try:
                item = FoodItem.objects.get(name=name)
            except FoodItem.DoesNotExist:
                item = None
            if item is not None:
                print("6")
                foodrest.food_item_id = item.food_item_id
            else:
                print("2")
                fooditem = FoodItem()
                fooditem.name = name
                is_veg = request.POST['is_veg']
                if is_veg == 1:
                    print("3")
                    fooditem.is_veg = True
                else:
                    print("4")
                    fooditem.is_veg = False
                fooditem.type_id = int(request.POST['type_id'])
                foodrest.food_item_id = fooditem.food_item_id
                fooditem.save()
                print("5")
            print("7")
            foodrest.restaurant = rest
            foodrest.cost = request.POST['cost']
            foodrest.save()
        else:

            foodid = int(request.POST['fooditemid'])
            try:
                food = FoodRestaurant.objects.get(food_item_id=foodid)
                food.delete()
            except FoodRestaurant.DoesNotExist:
                print("d")

    food = FoodRestaurant.objects.filter(restaurant=rest)
    menu = []
    for x in food:
        y = FoodItem.objects.get(food_item_id=x.food_item_id)
        cmenu = []
        cmenu.append(x.food_item_id)
        cmenu.append(y.name)
        cmenu.append(x.cost)
        cmenu.append(x.restaurant)
        cmenu.append(y.is_veg)

        print("yello")
        print(y.type)
        itype = ItemType.objects.get(type_id=y.type.type_id)
        cmenu.append(itype.name)
        cmenu.append(itype.type_id)
        if y.is_veg == 1:
            cmenu.append("veg")
        else:
            cmenu.append("non veg")
        menu.append(cmenu)

    i1 = ItemType.objects.all()
    itemtypes = []
    vegarray = [[0, "non veg"], [1, "veg"]]
    for x in i1:
        itemtypes.append([x.type_id, x.name])
    context = {
        "menu": menu,
        "user": request.user,
        "itemtypes": itemtypes,
        "vegarray": vegarray,
    }
    return render(request, 'webapp/menu_modify.html', context)

# # def orderlist(request):
# #     if request.POST:
# #         oid = request.POST['orderid']
# #         select = request.POST['orderstatus']
# #         select = int(select)
# #         order = Order.objects.filter(id=oid)
# #         if len(order):
# #             x = Order.ORDER_STATE_WAITING
# #             if select == 1:
# #                 x = Order.ORDER_STATE_PLACED
# #             elif select == 2:
# #                 x = Order.ORDER_STATE_ACKNOWLEDGED
# #             elif select == 3:
# #                 x = Order.ORDER_STATE_COMPLETED
# #             elif select == 4:
# #                 x = Order.ORDER_STATE_DISPATCHED
# #             elif select == 5:
# #                 x = Order.ORDER_STATE_CANCELLED
# #             else:
# #                 x = Order.ORDER_STATE_WAITING
# #             order[0].status = x
# #             order[0].save()
# #
# #     orders = Order.objects.filter(r_id=request.user.restaurant.id).order_by('-timestamp')
# #     corders = []
# #
# #     for order in orders:
# #
# #         user = User.objects.filter(id=order.orderedBy.id)
# #         user = user[0]
# #         corder = []
# #         if user.is_restaurant:
# #             corder.append(user.restaurant.rname)
# #             corder.append(user.restaurant.info)
# #         else:
# #             corder.append(user.customer.f_name)
# #             corder.append(user.customer.phone)
# #         items_list = orderItem.objects.filter(ord_id=order)
# #
# #         items = []
# #         for item in items_list:
# #             citem = []
# #             citem.append(item.item_id)
# #             citem.append(item.quantity)
# #             menu = Menu.objects.filter(id=item.item_id.id)
# #             citem.append(menu[0].price * item.quantity)
# #             menu = 0
# #             items.append(citem)
# #
# #         corder.append(items)
# #         corder.append(order.total_amount)
# #         corder.append(order.id)
# #
# #         x = order.status
# #         if x == Order.ORDER_STATE_WAITING:
# #             continue
# #         elif x == Order.ORDER_STATE_PLACED:
# #             x = 1
# #         elif x == Order.ORDER_STATE_ACKNOWLEDGED:
# #             x = 2
# #         elif x == Order.ORDER_STATE_COMPLETED:
# #             x = 3
# #         elif x == Order.ORDER_STATE_DISPATCHED:
# #             x = 4
# #         elif x == Order.ORDER_STATE_CANCELLED:
# #             x = 5
# #         else:
# #             continue
# #
# #         corder.append(x)
# #         corder.append(order.delivery_addr)
# #         corders.append(corder)
# #
# #     context = {
# #         "orders": corders,
# #     }
# #
# #     return render(request, "webapp/order-list.html", context)
