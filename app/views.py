from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm
from .models import Plan,Category

# Create your views here.
def index(request):
    return render(request,'app/index.html')
    

def plan_category(request,pk):
    planning=get_object_or_404(Plan,pk=pk)
    categol=get_object_or_404(Category,pk=pk)

    return render(request,'app/plans.html',{'planning':planning,'categol':categol})


def signup(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            input_email=form.cleaned_data['email']
            input_password=form.cleaned_data['password1']
            new_user=authenticate(email=input_email,password=input_password)
            if new_user is not None:
                login(request,new_user)
                return redirect('app:index')
            
    else:
        form=CustomUserCreationForm()
    return render(request,'app/signup.html',{'form':form})



# from django.views.generic import ListView

    # class Date(ListView):
#     model=Plan
#     templates_name='app/plan_list.html'
