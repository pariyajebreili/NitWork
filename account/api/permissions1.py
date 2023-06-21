from rest_framework.permissions import BasePermission


class IsCompany(BasePermission):
    def has_object_permission(self, request, view):
       return request.user.is_authenticated and request.user.is_company
        #return super().has_permission(request, view)
    

class IsStudent(BasePermission):
    def has_object_permission(self, request, view):      
        return bool(request.user and request.user.is_student)
