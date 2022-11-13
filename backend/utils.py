from rest_framework.permissions import BasePermission

from backend.models import UserAccount
from backend.serializers import UserAccountSerializer
from backend.tools import token2name


class hasOpPermission(BasePermission):

    def has_permission(self, request, view):
        token = request.header['token']
        CodeName = token2name(token)
        test = UserAccount.objects.get(CodeName=CodeName)
        serializer = UserAccountSerializer(instance=test)
        if serializer.data['Permission'] < 2:
            return True
