from django.db import models
from account.models import Company, Student, User
# Create your models here.



#class Comment(models.Model):
#    company=models.ForeignKey(Company,verbose_name=("company"),related_name="comments",on_delete=models.CASCADE)
#    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="comments")
#    message=models.TextField()
#    date=models.DateField(auto_now=False,auto_now_add=True)


#    def __str__(self):
#        return self.company.name

class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    likeuser=models.ForeignKey(Company,related_name="like",on_delete=models.CASCADE)
    likecompany=models.ForeignKey(Student,related_name="likes",on_delete=models.CASCADE,null=True)


class Dislike(models.Model):
    dislikeuser=models.ForeignKey(Company,related_name="Dislike",on_delete=models.CASCADE)
    dislikecompany=models.ForeignKey(Student,related_name="Dislikes",on_delete=models.CASCADE,null=True)








