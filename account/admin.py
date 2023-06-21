from django.contrib import admin
from .models import User, Student, Company
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Company)