from rest_framework import serializers

from backend.models import UserAccount, UserProfile, AccountApproveQueue, Passage


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    # 这里可以动态添加属性
    class Meta:
        model = UserProfile
        fields = "__all__"


class AccountApproveQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountApproveQueue
        fields = "__all__"


class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = "__all__"
