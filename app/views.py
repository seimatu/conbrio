from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm,PlanForm
from .models import Plan,Category
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def plans(request):
    plans=Plan.objects.all().order_by('-created_at')
    return render(request,'app/plans.html',{'plans':plans})


def plan_list(request,pk):
    categol=get_object_or_404(Category,pk=pk)
    planning=categol.plan_set.all().order_by('-creates_at')

    return render(request,'app/plan_list.html',{'planning':planning,'categol':categol})



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


@login_required
def plans_new(request):
    if request.method=="POST":
        form=PlanForm(request.POST,request.FILES)
        if form.is_valid():
            plan=form.save(commit=False)
            plan.user=request.user
            plan.save()
        return redirect('app:plan_list',pk=request.plan.pk)
    else:
        form=PlanForm()
    return render(request,'app/plans_new.html',{'form':form})

