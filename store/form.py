from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction

from store.models import User, Position, Employee, Supplier, Drug


class EmployeeSignUpForm(UserCreationForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(EmployeeSignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    # def clean_position(self):
    #     position_name = self.cleaned_data['position']
    #     # check the name if you need to
    #     try:
    #         # maybe check if it already exists?
    #         position = Employee.objects.get(name=position_name)
    #     except Employee.DoesNotExist:
    #         position = Position(name=position_name)
    #         # you probably only want to save this when the form is saved (in the view)
    #     return position

    @transaction.atomic
    def save(self):
        user = super(EmployeeSignUpForm, self).save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user, position=self.cleaned_data['position'])
        employee.save()
        return user


class SupplierSignUpForm(UserCreationForm):
    name = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(SupplierSignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    @transaction.atomic
    def save(self):
        user = super(SupplierSignUpForm, self).save(commit=False)
        user.is_supplier = True
        user.save()
        supplier = Supplier.objects.create(user=user)
        supplier.name = self.cleaned_data.get('name')
        supplier.address = self.cleaned_data.get('address')
        supplier.save()
        return user


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DrugForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'