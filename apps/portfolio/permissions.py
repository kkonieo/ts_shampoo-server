from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자가 작성자인지
        if obj.author == request.user:
            return True
