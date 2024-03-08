
from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    """
    Права доступа для владельца урока/курса
    """
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsModerator(BasePermission):
    """
    Права доступа для модератора
    """
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.job_title == 'Moderator':
            return True
        return False