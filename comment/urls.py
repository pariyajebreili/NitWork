from django.urls import path
from comment import views
from .views import ShowCommentView,SendCommentView
from django.urls import path, include
from rest_framework import routers

app_name='comments'

urlpatterns=[
    path('send_comment/<int:id_company>/', SendCommentView.as_view(), name='send_comment'),
    path("show_comment/<int:id_company>/",ShowCommentView.as_view(),name='show_comment'),
]
