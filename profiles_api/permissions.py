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

### To fix the error that appears when trying to delete an object
### without being authenticated

#users only can update objects in their own account
class  UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self,request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # Make sure that the user own that status
        return obj.user_profile.id == request.user.id
        # if it is true the request is done otherwise
        # the request is blocked
