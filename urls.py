from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.loginpage,name="loginpage"),
    path('admin_page',views.admin_page,name="admin_page"),
    path('employee_page',views.employee_page,name="employee_page"),

]
