from rest_framework import permissions


class IsPostOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
