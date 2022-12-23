import json

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.tools import get_jwt, fail, token2name
from .serializers import UserAccountSerializer, AccountApproveQueue, \
    AccountApproveQueueSerializer, UserProfileSerializer, PassageSerializer
from .models import UserAccount, UserProfile, Passage
from .utils import hasOpPermission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize


class loginView(GenericAPIView, CreateModelMixin):
    queryset = AccountApproveQueue.objects.all()
    serializer_class = AccountApproveQueueSerializer

    def post(self, request, module):

        if module == 'login':
            data = request.data
            try:
                print(data)
                user = UserAccount.objects.get(CodeName=data['CodeName'])
                print(user)
                if data['Password'] == user.Password:
                    token = get_jwt(user.CodeName)
                    result = {'CodeName': user.CodeName, 'token': token}
                    return Response(result)
                else:
                    return Response(fail('密码错误'), status=403)
            except UserAccount.DoesNotExist:
                return Response(fail('用户不存在'), status=404)

        if module == 'enroll':
            return self.create(request)


class UserListView(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    # permission_classes = [hasOpPermission, ]

    def get(self, request):
        print(request.data)
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UserDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'CodeName'

    def put(self, request, CodeName):
        return self.update(request)

    def get(self, request, CodeName):
        return self.retrieve(request)

    def delete(self, request, CodeName):
        return self.destroy(request)


class ApplicationOtherView(GenericAPIView, CreateModelMixin, DestroyModelMixin):
    flag = 0
    lookup_field = 'CodeName'

    def post(self, request, CodeName):
        self.flag = 0
        result = self.create(request)
        self.flag = 1
        return self.destroy(request)

    def get_serializer_class(self):
        if self.flag == 0:
            return UserAccountSerializer
        else:
            return AccountApproveQueueSerializer

    def get_queryset(self):
        if self.flag == 0:
            return UserAccount.objects.all()
        else:
            return AccountApproveQueue.objects.all()


class ApplicationModelView(ModelViewSet):
    queryset = AccountApproveQueue.objects.all()
    serializer_class = AccountApproveQueueSerializer
    lookup_field = 'CodeName'
    lookup_url_kwarg = 'CodeName'


class ProfileListView(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'CodeName'

    # permission_classes = [hasOpPermission, ]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProfileDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'CodeName'

    def put(self, request, CodeName):
        return self.update(request)

    def get(self, request, CodeName):
        return self.retrieve(request)

    def delete(self, request, CodeName):
        return self.destroy(request)


class PassageListView(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    lookup_field = 'PId'

    def get(self, request, idx):
        paginator = Paginator(self.queryset, 5)  # 5 posts per page
        pageObj = []
        try:
            ret_list = paginator.page(idx)
            ret_list = serialize('json', ret_list.object_list)
            ret_list = json.loads(ret_list)
            print(ret_list)
            for i in ret_list:
                i['fields']['PId'] = i['pk']
                pageObj.append(i['fields'])
            print(pageObj)
            result = {"pageIdx": idx, "pageObj": pageObj, "totalPage": paginator.num_pages}
        except PageNotAnInteger:
            ret_list = paginator.page(1)
            ret_list = serialize('json', ret_list.object_list)
            ret_list = json.loads(ret_list)
            for i in ret_list:
                i['fields']['PId'] = i['pk']
                pageObj.append(i['fields'])
            result = {"pageIdx": 1, "pageObj": pageObj, "totalPage": paginator.num_pages}
        except EmptyPage:
            ret_list = paginator.page(paginator.num_pages)
            ret_list = serialize('json', ret_list.object_list)
            ret_list = json.loads(ret_list)
            for i in ret_list:
                i['fields']['PId'] = i['pk']
                pageObj.append(i['fields'])
            result = {"pageIdx": paginator.num_pages, "pageObj": pageObj, "totalPage": paginator.num_pages}

        return Response(result)

    def post(self, request):
        print(request.data)
        return self.create(request)


class PassageDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    lookup_field = 'PId'

    def put(self, request, PId):
        return self.update(request)

    def get(self, request, PId):
        return self.retrieve(request)

    def delete(self, request, PId):
        return self.destroy(request)


# 后端调试使用
def index(request):
    return render(request, 'testbackend.html')


def log(request):
    return render(request, 'login.html')


class SelfView(GenericAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'CodeName'

    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        CodeName = token2name(token)
        userAccount = UserAccount.objects.get(CodeName=CodeName)
        serializer = UserAccountSerializer(instance=userAccount)
        return Response(serializer.data)


class testView(GenericAPIView, RetrieveModelMixin, CreateModelMixin, ListModelMixin):
    querysetFlag = 0
    lookup_field = 'CodeName'

    def get_queryset(self):
        if self.querysetFlag == 0:
            return UserAccount.objects.all()
        else:
            return AccountApproveQueue.objects.all()

    def get_serializer_class(self):
        if self.querysetFlag == 0:
            return UserAccountSerializer
        else:
            return AccountApproveQueueSerializer

    def get(self, request, CodeName):
        self.querysetFlag = 0
        data = self.retrieve(request).data
        self.queryset = 1
        request.data.update(data)
        return self.create(request)
