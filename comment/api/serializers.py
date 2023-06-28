from rest_framework import routers, serializers, viewsets
from ..models import Comment,Like,Dislike
from account.models import Company



class Comment_serializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["message"]  


class Show_Comment_serializers(serializers.ModelSerializer):
        
    class Meta:
        model=Comment
        fields=["id","user","message","date"]  



class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__ '     

class dislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['dislikeuser']    


