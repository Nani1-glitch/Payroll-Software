from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('employees/', views.employees,name="employees"),
    path('departments/', views.departments,name="departments"),
    path('payrolls/', views.payrolls,name="payrolls"),
]