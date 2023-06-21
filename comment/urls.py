from django.urls import path
from comment import views
from .views import ShowCommentView,SendCommentView

app_name='comments'

urlpatterns=[
    path('send_comment/<int:id_company>/', SendCommentView.as_view(), name='send_comment'),
    #path("delete/<c_id>",views.delete_comment,name='delete_comment'),
    path("show_comment/<int:id_company>/",ShowCommentView.as_view(),name='show_comment'),
    #path("like/<f_id>",views.like,name='like'),
    #path("dislike/<f_id>",views.dislike,name='dislike'),
]
