from django.contrib import admin
from django.urls import path

from store.views import register, EmployeeRegister, SupplierRegister, HomeView, HomeDetailView, DrugCreateView, \
    login_request, logout_view

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('register/', register, name='register_page'),
    path('employee/register/', EmployeeRegister.as_view(), name='employee_register_page'),
    path('supplier/register/', SupplierRegister.as_view(), name='supplier_register_page'),
    path('login/', login_request, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('detail/<int:pk>', HomeDetailView.as_view(), name='detail_page'),
    path('edit/', DrugCreateView.as_view(), name='edit_page'),
]
