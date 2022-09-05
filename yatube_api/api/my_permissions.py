from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.author == request.user
