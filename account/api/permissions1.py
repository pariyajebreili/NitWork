from rest_framework.permissions import BasePermission


class IsClientUser(BasePermission):
    def has_object_permission(self, request, view):
       return request.user.is_authenticated and request.user.is_client
        #return super().has_permission(request, view)
    

class IsFreelanceUser(BasePermission):
    def has_object_permission(self, request, view):      
        return bool(request.user and request.user.is_freelancer)
