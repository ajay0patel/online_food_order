
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
	path("desk",admin.site.urls),
    path("admin/",adminloginview,name="adminloginpage"),
    path("authenticateadmin/", authenticateadmin),
    path("admin/homepage/",adminhomepageview,name="adminhomepage"),
    path("adminlogout/",logoutadmin),
    path("addpizza/",addpizza),
    path("deletepizza/<int:pizzapk>",deletepizza),
    path("",homepageview,name="homepage"),
    path("signupuser/",signupuser),
    path("loginuser/",userloginview,name="userloginpage"),
    path("customer/welcome/",customerwelcomeview,name="customerpage"),
    path("customer/authenticate/",userauthenticate),
    path("userlogout/",userlogout),
    path("placeorder/",placeorder),
    path("myorders/",myorders),
    path("adminallorders/",allorders),
    path("acceptorder/<int:orderpk>/",acceptorder),
    path("declineorder/<int:orderpk>/",declineorder)
]
