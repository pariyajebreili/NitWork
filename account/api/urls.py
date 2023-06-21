from django.urls import path
from . import views
from .views import FreelanceSignupView, ClientSignupView, FreelanceOnlyView, ClientOnlyView,user_LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('signup/freelancer/', FreelanceSignupView.as_view()),
    path('signup/client/', ClientSignupView.as_view()),
    path('login/',user_LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('freelance/dashbord/',FreelanceOnlyView.as_view()),
    path('client/dashboard/',ClientOnlyView.as_view()),
]
