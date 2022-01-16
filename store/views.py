from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from store import models
from store.form import EmployeeSignUpForm, SupplierSignUpForm, DrugForm, ComponentForm
from store.models import User, Drug, Component


def register(request):
    template = 'register.html'
    return render(request, template_name=template)


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


class EmployeeRegister(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'employee_register.html'

    # def form_valid(self, form):
    #     if form.is_valid():
    #         employee = form.save()
    #         position = form.cleaned_data['position']
    #         employee.position = position
    #         employee.save()
    #         form.save()
    #         return HttpResponseRedirect('/')


class SupplierRegister(CreateView):
    model = User
    form_class = SupplierSignUpForm
    template_name = 'supplier_register.html'


class CustomSuccessMessageMixin:
    @property
    def success_message(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(CustomSuccessMessageMixin, self).form_valid(form)

    def get_success_url(self):
        return f'{self.success_url}?id={self.object.id}'


class HomeView(ListView):
    model = Drug
    template_name = 'index.html'
    context_object_name = 'queryset'


class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Drug
    template_name = 'detail.html'
    context_object_name = 'get_drug'


def edit_view(request):
    return render(request, 'edit.html')


class DrugCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = Drug
    template_name = 'edit_drug.html'
    form_class = DrugForm
    success_url = reverse_lazy('edit_drug')
    success_message = "Record Created"

    def get_context_data(self, **kwargs):
        kwargs['queryset'] = Drug.objects.all().order_by('id')
        return super(DrugCreateView, self).get_context_data(**kwargs)


class DrugUpdateView(UpdateView):
    model = Drug
    template_name = 'edit_drug.html'
    form_class = DrugForm
    success_url = reverse_lazy('edit_drug')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super(DrugUpdateView, self).get_context_data(**kwargs)


def delete_drug(requst, pk):
    get_company = Drug.objects.get(pk=pk)
    get_company.delete()

    return redirect(reverse('edit_drug'))


class ComponentCreateView(LoginRequiredMixin, CreateView):
    model = Component
    template_name = 'edit_component.html'
    form_class = ComponentForm
    success_url = reverse_lazy('edit_component')
    success_message = 'Record Created'

    def get_context_data(self, **kwargs):
        kwargs['queryset'] = Component.objects.all().order_by('id')
        return super(ComponentCreateView, self).get_context_data(**kwargs)


class ComponentUpdateView(UpdateView):
    model = Component
    template_name = 'edit_component.html'
    form_class = ComponentForm
    success_url = reverse_lazy('edit_component')

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super(ComponentUpdateView, self).get_context_data(**kwargs)


def delete_component(requst, pk):
    get_company = Component.objects.get(pk=pk)
    get_company.delete()

    return redirect(reverse('edit_component'))


