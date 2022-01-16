from django.contrib import admin
from django.urls import path

from store.views import register, EmployeeRegister, SupplierRegister, HomeView, HomeDetailView, DrugCreateView, \
    login_request, logout_view, edit_view, ComponentCreateView, DrugUpdateView, delete_drug, ComponentUpdateView, delete_component

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('register/', register, name='register_page'),
    path('employee/register/', EmployeeRegister.as_view(), name='employee_register_page'),
    path('supplier/register/', SupplierRegister.as_view(), name='supplier_register_page'),
    path('login/', login_request, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('detail/<int:pk>', HomeDetailView.as_view(), name='detail_page'),
    path('edit', edit_view, name='edit'),
    path('edit_drug/', DrugCreateView.as_view(), name='edit_drug'),
    path('update_drug/<int:pk>', DrugUpdateView.as_view(), name='update_drug'),
    path('delete_drug/<int:pk>', delete_drug, name='delete_drug'),
    path('edit_component/', ComponentCreateView.as_view(), name='edit_component'),
    path('update_component/<int:pk>', ComponentUpdateView.as_view(), name='update_component'),
    path('delete_component/<int:pk>', delete_component, name='delete_component'),
]
