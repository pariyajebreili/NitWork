from django.urls import path
from . import views
from .views import FreelanceSignupView, ClientSignupView, CustomAuthToken, FreelanceOnlyView, ClientOnlyView, LogoutView


urlpatterns = [
    path('signup/freelancer/', FreelanceSignupView.as_view()),
    path('signup/client/', ClientSignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('freelance/dashbord/',FreelanceOnlyView.as_view()),
    path('client/dashboard/',ClientOnlyView.as_view()),
]