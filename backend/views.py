from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.tools import get_jwt, token2name
from .serializers import UserAccountSerializer, AccountApproveQueue, \
    AccountApproveQueueSerializer
from .models import UserAccount


class loginView(GenericAPIView, CreateModelMixin):
    queryset = AccountApproveQueue.objects.all()
    serializer_class = AccountApproveQueueSerializer

    def post(self, request, module):
        if module == 'login':
            data = request.data
            user = UserAccount.objects.get(CodeName=data['CodeName'])
            if data['Password'] == user.Password:
                token = get_jwt(user.CodeName)
                result = {'CodeName': user.CodeName, 'token': token}
                return Response(result)
            else:
                return Response('登录失败')
        if module == 'enroll':
            return self.create(request)


class UserListView(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    # permission_classes = [hasOpPermission, ]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UserDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'CodeName'

    def put(self, request, CodeName):
        print(CodeName + '\n\n\n\n')
        return self.update(request)

    def get(self, request, CodeName):
        return self.retrieve(request)

    def delete(self, request, CodeName):
        return self.destroy(request)


class ApplicationModelView(ModelViewSet):
    queryset = AccountApproveQueue.objects.all()
    serializer_class = AccountApproveQueueSerializer
    lookup_field = 'CodeName'
    lookup_url_kwarg = 'CodeName'


# 后端调试使用
def index(request):
    return render(request, 'testbackend.html')


def log(request):
    return render(request, 'login.html')
