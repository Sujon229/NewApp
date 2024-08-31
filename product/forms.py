from django import forms
from .models import Product
from .models import User

class ProductEntry(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','describe','price']

class UserEntry(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname','lname','email','password']