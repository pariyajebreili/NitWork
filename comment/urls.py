from django.urls import path
from comment import views

app_name='comments'

urlpatterns=[
    path('send_comment/<str:identifier>/', views.send_comment, name='send_comment'),
    #path("delete/<c_id>",views.delete_comment,name='delete_comment'),
    #path("show_comment/<f_id>",views.show_comment,name='show_comment'),
    #path("like/<f_id>",views.like,name='like'),
    #path("dislike/<f_id>",views.dislike,name='dislike'),
]
