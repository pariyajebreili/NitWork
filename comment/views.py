
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import Comment_serializers,Show_Comment_serializers,likeSerializer,dislikeSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import filters
from rest_framework import generics
import datetime
from django.db.models import Q
from account.models import Student, Company, User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
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



class SendCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id_company):
        company = Company.objects.get(id=id_company)

        new_comment = Comment_serializers(data=request.data)
        if new_comment.is_valid():
            date1 = datetime.now()
            student = request.user.student
            user = student.user
            new_comment2 = Comment(company=company, user=user, message=new_comment.validated_data["message"], date=date1)
            new_comment2.save()
            n_comment = Show_Comment_serializers(instance=new_comment2)

            return Response({
                'message': 'Comment saved successfully',
                'status': 'success',
                'comment_for_company': company.id,
                'comment': n_comment.data,
            }, status=status.HTTP_201_CREATED)

        return Response(new_comment.errors, status=status.HTTP_400_BAD_REQUEST)



class ShowCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_company):
        try:
            company = Company.objects.get(id=id_company)
        except company.DoesNotExist:
            raise NotFoundError('Company not found.')

        comments = company.comments.all()
        comment_serialize = Show_Comment_serializers(instance=comments, many=True)

        return Response({"comments": comment_serialize.data})

  

