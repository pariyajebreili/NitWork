
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Comment,Like,Dislike
from .serializers import Comment_serializers,Show_Comment_serializers,likeSerializer,dislikeSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import filters
from rest_framework import generics
import datetime
from django.db.models import Q
from account.models import Student, Company
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Company, Comment
from rest_framework.exceptions import APIException
from rest_framework import status


class NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'The requested resource was not found.'
    default_code = 'not_found'



@permission_classes([IsAuthenticated])
@api_view(["POST"])       
def send_comment(request, id_company):
    try:
        company = Company.objects.get(id=id_company)

    except Company.DoesNotExist:
        raise NotFoundError('Company not found.')
    
    company = Company.objects.get(id=id_company)

    if request.method == "POST":
        new_comment = Comment_serializers(data=request.data)
        if new_comment.is_valid(raise_exception=True):
            date1 = datetime.now()
            student = request.user.student  # assuming request.user is a Student object
            user = student.user  # get the User object associated with the Student object
            new_comment2 = Comment(company=company, user=user, message=new_comment.data["message"], date=date1)
            new_comment2.save()
            n_comment = Show_Comment_serializers(instance=new_comment2)
            return Response({
                'message': 'Comment saved successfully',
                'status': 'success',
                'comment_for_company': company.id,
                'comment': n_comment.data,
            }, status=status.HTTP_201_CREATED)

        return Response(new_comment.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
@permission_classes([IsAuthenticated])                
def show_comment(request,id_company):

    try:
        company=Company.objects.get(id=id_company)

    except company.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    comment=company.comments

    c_serialize=Show_Comment_serializers(instance=comment,many=True)

    return Response({"comments":c_serialize.data})


  


##@api_view(["DELETE"])
###@permission_classes([IsAuthenticated])
##def delete_comment(request,c_id):           
##    serializer = AuthTokenSerializer(data=request.data)
##    if(serializer.is_valid(raise_exception=True)):
##        try:
##            comment=Comment.objects.get(id=c_id)
##            if comment.user==request.user:
##                comment.delete()
##                return Response({"message":"comment deleted!!"})
##            else:
##                return Response({"message":"you dont delete this comment!!"},status=status.HTTP_400_BAD_REQUEST)


##        except comment.DoesNotExist:
##            if comment is None:
##                return Response({"message":"this comment not exist!!"},status=status.HTTP_404_NOT_FOUND) 
##    else:
##        print("authenticate")




#@api_view(["GET"])
##@permission_classes([IsAuthenticated])            
#def like(request,f_id):
#    serializer = AuthTokenSerializer(data=request.data)
#    if(serializer.is_valid(raise_exception=True)):
#        try:
#            likeuser = UserProfile.objects.get(id=request.user.id)

#        except likeuser.DoesNotExist:
#            return Response(status=status.HTTP_400_BAD_REQUEST)
        
#        try:
#            likecompany = CompanyProfile.objects.get(id=f_id)

#        except likecompany.DoesNotExist:
#            return Response(status=status.HTTP_400_BAD_REQUEST)


#        check = Like.objects.filter(likeuser=likeuser).filter(likecompany=likecompany)
#        if(check.exists()):

#            check.delete()
#            if likecompany.rate >= 1:
#                likecompany.rate-=1
#                likecompany.save()
#            return Response({
#                "message":"Unliked!!"
#                })
        
#        new_like = Like.objects.create(likeuser=likeuser, likecompany=likecompany)
#        new_like.save()
#        likecompany.rate+=1
#        likecompany.save()
#        serializer = likeSerializer(new_like)

#        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
#    else:
#        print("authenticate")







#@api_view(["GET"])
##@permission_classes([IsAuthenticated])                
#def dislike(request,f_id):
#    serializer = AuthTokenSerializer(data=request.data)
#    if(serializer.is_valid(raise_exception=True)):
#        try:

#            dislikeuser = UserProfile.objects.get(id=request.user.id)

#        except dislikeuser.DoesNotExist:
#            return Response(status=status.HTTP_400_BAD_REQUEST)
        
#        try:

#            dislikefood = CompanyProfile.objects.get(id=f_id)

#        except dislikefood.DoesNotExist:
#            return Response(status=status.HTTP_400_BAD_REQUEST)


#        check = Dislike.objects.filter(dislikeuser=dislikeuser).filter(dislikefood=dislikefood)
#        if(check.exists()):
#            if dislikefood.negative_rate >= 1:
#                dislikefood.negative_rate-=1
#                dislikefood.save()
#            check.delete()
#            return Response({
#                "message":"Undisliked!!"
#                })
        
#        new_dislike = Dislike.objects.create(dislikeuser=dislikeuser, dislikefood=dislikefood)
#        new_dislike.save()
        
#        dislikefood.negative_rate+=1
#        dislikefood.save()
#        serializer = dislikeSerializer(new_dislike)

#        return Response(serializer.data,status=status.HTTP_201_CREATED)
#    else:
#        print("authenticate")






