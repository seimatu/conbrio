from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='app'

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/',views.detail,name='detail'),
    path('city/<str:city_name>/',views.city,name='city'),
    path('plans/new/',views.plans_new,name='plans_new'),
    path('plan_list/<str:plan_categories>/',views.plan_list,name='plan_list'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),
    name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
