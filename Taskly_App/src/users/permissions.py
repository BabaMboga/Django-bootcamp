from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permissions for UserViewSet to only allow user to edit their own profile, Otherwise Get and Post only.
    """