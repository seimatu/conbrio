from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm,PlanForm
from .models import Plan,Category
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    plan=Plan.objects.all()
    return render(request,'app/index.html',{'plan':plan})

def user_detail(request):
    return render(request,'app/user_detail.html')

def all_plans(request,pk):
    plans=get_object_or_404(User,pk=pk)
    planic=Plan.objects.all().order_by('-created_at')
    return render(request,'app/all_plans.html',{'planic':planic,'plans':plans})

def plan_list(request,plan_categories):
    plan_categories=Category.objects.get(title=plan_categories)
    planning=Plan.objects.filter(plan_categories=plan_categories).order_by('-created_at')
    return render(request,'app/plan_list.html',{'planning':planning,'plan_categories':plan_categories})

def signup(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            input_name=form.cleaned_data['sirname']
            input_email=form.cleaned_data['email']
            input_password=form.cleaned_data['password1']
            new_user=authenticate(name=input_name,email=input_email,password=input_password)
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
            plan.plan_user=request.user
            plan.save()
        return redirect('app:all_plans', pk=request.user.pk)
    else:
        form=PlanForm()
    return render(request,'app/plans_new.html',{'form':form})

