from django.contrib import admin
from .models import User, Freelancer, Client
# Register your models here.

admin.site.register(User)
admin.site.register(Freelancer)
admin.site.register(Client)