from rest_framework import serializers

from backend.models import UserAccount, UserProfile, AccountApproveQueue, Passage, Message, Group, OperatorGroup, Reply


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


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class OperatorGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatorGroup
        fields = "__all__"


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"
