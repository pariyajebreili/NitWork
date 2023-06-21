from django.urls import path
from . import views
from .views import StudentSignupView, CompanySignupView, CompanyOnlyView, StudentOnlyView,user_LoginAPI, StudentUpdateView, CompanyUpdateView
from knox import views as knox_views

urlpatterns = [
    path('signup/student/', StudentSignupView.as_view()),
    path('signup/company/', CompanySignupView.as_view()),
    path('login/',user_LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('comapny/dashbord/',CompanyOnlyView.as_view()),
    path('student/dashboard/',StudentOnlyView.as_view()),
    path('student_update/',StudentUpdateView.as_view()),
    path('company_update/',CompanyUpdateView.as_view()),
]
