from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Customer, RestaurantOwner, Location, Restaurant


class CategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "Category: {}".format(obj.name)


class CustomerRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_customer = True
            if commit:
                user.save()
            return user


class CustomerRegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['f_name', 'l_name', 'addressline1', 'phone', 'addressline2', 'location']


class RestaurantRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_restaurant_owner = True
            if commit:
                user.save()
            return user


class RestaurantRegisterProfileForm(forms.ModelForm):
    class Meta:
        model = RestaurantOwner
        fields = ['f_name', 'l_name', 'addressline1', 'phone', 'addressline2', 'location']


# class RestaurantDetailForm(forms.ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = ['name', 'address', 'avg_cost', 'avg_time', 'phone', 'r_logo']

class RestaurantDetailForm(forms.ModelForm):
    # field1 = forms.ModelChoiceField(queryset=Location.objects.all())
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'avg_cost', 'avg_time', 'phone', 'r_logo', 'location')



# def formfield_for_foreignkey(self, db_field, request, **kwargs):
#     if db_field.name == 'location':
#         return CategoryChoiceField(queryset=Location.objects.all())
#     return super().formfield_for_foreignkey(db_field, request, **kwargs)

# class RestuarantOwnerSignUpForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)
# 	class Meta:
# 		model =User
# 		fields=['username','email','password']
# 		def save(self,commit=True):
# 			user=super().save(commit=False)
# 			user.is_restaurant=True
# 			if commit:
# 				user.save()
# 			return user

# class CustomerForm(forms.ModelForm):
# 	class Meta:


# class RestuarantForm(forms.ModelForm):
# 	class Meta:
# 		model = Restaurant
# 		fields =['rname','info','location','r_logo','min_ord','status','approved']
#
#
#
#
#
#
#
#
#
