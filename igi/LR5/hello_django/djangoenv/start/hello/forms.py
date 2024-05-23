from django import forms
from .models import Specialization
 
class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    phone_number = forms.CharField()

class LoginForm(forms.Form):
    is_master = forms.BooleanField()
    name = forms.CharField()

class RegisterSpecializations(forms.Form):
    specializations = forms.ChoiceField(
        choices=[(spec.id, spec.name) for spec in Specialization.objects.all()],
        widget=forms.Select
    )