from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import CustomUsers


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUsers
        fields = ('username','first_name','last_name','email','age')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUsers
        fields = ('username','first_name','last_name','email','age')        