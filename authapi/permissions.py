from rest_framework.permissions import BasePermission
from authapi.models import User

'''
Permissions as implemented by the AuthorityMatrix.
'''

class CanSendVerifiers(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['IN']


class CanViewVerifiers(BasePermission):
    def has_permission(self, request, view):
        #print(request.user)
        return request.user.role in ['IN', 'EU']

