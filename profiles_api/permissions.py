from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        ### Enables only to do safe methods as for example
        ### the GET method
        if request.method in permissions.SAFE_METHODS:
            return True

        ### If the method that is intended to be done is not a
        ## safe method, this can only be done if the user try to do it
        ## to his own profile and not to the other profile
        return obj.id == request.user.id 
