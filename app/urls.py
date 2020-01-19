from django.urls import path
from . import views
# from .views import Date
from django.contrib.auth import views as auth_views

app_name='app'

urlpatterns = [
    path('',views.index,name='index'),
    path('plans/<int:pk>/',views.plan_category,name='plans'),
    # path('date/',Date.as_view(),name='plan_list'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),
    name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

]
