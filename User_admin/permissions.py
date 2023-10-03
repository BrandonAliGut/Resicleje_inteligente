from rest_framework import permissions
from django.http.response import HttpResponse
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.request import Request
class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print#(obj.id) print(request.user)
        return obj.id == request.user.id
        
def permission_denied(self, request, message=None, code=None):
    """
    If request is not permitted, determine what kind of exception to raise.
    """
    if request.authenticators and not request.successful_authenticator:
        raise exceptions.NotAuthenticated()
    raise exceptions.PermissionDenied(detail=message, code=code)
