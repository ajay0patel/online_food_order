from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import *

import json
# Create your views here.

def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")

# admin login
def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username= username , password = password)

    if user is not None and user.username=="admin":
        login(request,user)
        return redirect('adminhomepage')

    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Username or Password")
        return redirect('adminloginpage')

def adminhomepageview(request):
    #after adding pizza -->for display
    context = {'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaapp/adminhomepage.html",context)

#admin logout
def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    #code for adding pizza to database
    name = request.POST['pizza']
    price = request.POST['price']

    PizzaModel(name=name , price= price).save()

    return redirect('adminhomepage')

def deletepizza(request,pizzapk):
    PizzaModel.objects.filter(id = pizzapk).delete()

    return redirect('adminhomepage')

def homepageview(request):
    return render(request,"pizzaapp/homepage.html")

def signupuser(request):
    uname = request.POST['username']
    pas = request.POST['password']
    pno = request.POST['phoneno']

    #django.contrib.auth.models import User

    #if user name exist
    if User.objects.filter(username = uname).exists():
        messages.add_message(request,messages.ERROR,"User Already Exists")
        return redirect('homepage')

    #if user not exist
    User.objects.create_user(username = uname,password=pas).save()
    lastobj = len(User.objects.all())-1
    CustomerModel(userid= User.objects.all()[int(lastobj)].id , phonno = pno)
    #CustomerModel(userid= User.objects.all()[int(lastobj)].id , phonno = pno).save()
    messages.add_message(request,messages.ERROR,"User Successfully Created")
    return redirect('homepage')

def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username= username , password = password)

    if user is not None:
        login(request,user)
        return redirect('customerpage')

    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Username or Password")
        return redirect('userloginpage')

def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')

    username = request.user.username
    context = {'username' : username , 'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaapp/customerwelcome.html",context)

def userlogout(request):
    logout(request)
    return redirect("userloginpage")

def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')

    username = request.user.username
    phoneno = request.POST['pno']
    address = request.POST['address']

    ordereditems = ''
    amount = 0

    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid)," ")

        if str(quantity)!='0' and str(quantity)!='':
            ordereditems +='{'+'"Name"'+':'+ '"'+name+'"' +','+ '"Price"'+':'+ str(int(price)*int(quantity)) + ',' + '"Quantity"'+':'+ quantity +'}'
            amount+=int(price)*int(quantity)

    OrderModel(username=username,phonno=phoneno,address=address,ordereditems=ordereditems,status="Pending",totalAmount=amount).save()

    messages.add_message(request,messages.ERROR,"Order Successfully Placed")
    return redirect('customerpage')

def myorders(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')

    curr_user = request.user.username

    order_data = OrderModel.objects.filter(username = curr_user)

    '''lis=[]
    for item in order_data:
        ordered_item = item.ordereditems
        print(ordered_item)

        l=len(ordered_item)

        j=0

        for i in range(l):
            if ordered_item[i]=='}':
                temp_str=ordered_item[j:i+1]
                j=i+1
                res = json.loads(temp_str)
                lis.append(res)
'''

    context = {
        'orders' : order_data,
        'user_name' : curr_user,
        }
    return render(request,"pizzaapp/myorders.html",context)

def allorders(request):
    order_data = OrderModel.objects.all()

    context = {
        'orders' : order_data
        }

    return render(request,"pizzaapp/allorders.html",context)

def acceptorder(request,orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "Accepted"
    order.save()

    return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "Declined"
    order.save()

    return redirect(request.META['HTTP_REFERER'])
    pass
