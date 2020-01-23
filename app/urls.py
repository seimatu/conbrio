from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='app'

urlpatterns = [
    path('',views.index,name='index'),
    path('user_detail/',views.user_detail,name='user_detail'),
    path('all_plans/<int:pk>/',views.all_plans,name='all_plans'),
    path('plans/new/',views.plans_new,name='plans_new'),
    path('plan_list/<str:plan_categories>/',views.plan_list,name='plan_list'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),
    name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
