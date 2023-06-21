
#from rest_framework.decorators import api_view,permission_classes
#from rest_framework.response import Response
#from rest_framework import status
#from .models import Comment,Like,Dislike
#from .serializers import Company_serializers,Comment_serializers,Show_Comment_serializers,likeSerializer,dislikeSerializer
#from rest_framework.permissions import IsAuthenticated,IsAdminUser
#from rest_framework import filters
#from rest_framework import generics
#import datetime
#from django.db.models import Q
#from account.models import Student, Company
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authtoken.serializers import AuthTokenSerializer


#@permission_classes([IsAuthenticated])    
#@api_view(["POST"])       
#def send_comment(request,f_id):

#    try:
#        company=Company.objects.get(id=f_id)
#    except company.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

#    User = UserProfile()
#    authenticated_user = User.objects.get(id=user.id)
#    UserProfile.objects.all()
#    #UserProfile = authenticated_user.userprofile 
#    new_comment=Comment_serializers(data=request.data)
#    if new_comment.is_valid(raise_exception=True):

#        date1=datetime.datetime.now()
#        user = request.user
#        new_comment2=Comment(company=company,user=UserProfile,message=new_comment.data["message"],date=date1)

#        new_comment2.save()
#        n_comment=Show_Comment_serializers(instance=new_comment2)
#        return Response({'message':'comment saved succsesfully','status':'success','comment_for_company':company.company_id,'comment':n_comment.data,
#        },status=status.HTTP_201_CREATED)

#    return Response(new_comment.errors)



#@api_view(["GET"])
##@permission_classes([IsAuthenticated])                
#def show_comment(request,f_id):

#    try:
#        company=CompanyProfile.objects.get(id=f_id)

#    except company.DoesNotExist:

#        return Response(status=status.HTTP_404_NOT_FOUND) 

#    comment=company.comments

#    c_serialize=Show_Comment_serializers(instance=comment,many=True)

#    return Response({"comments":c_serialize.data})


  


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






