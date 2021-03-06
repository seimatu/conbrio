from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('email','sirname',)


from django.forms import ModelForm
from .models import Plan

class PlanForm(ModelForm):
    class Meta:
        model=Plan
        fields=['plan_title','plan_categories','image','city_name','first_place','second_place','totaltime',]