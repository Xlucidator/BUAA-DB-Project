from django.db import models
import datetime


# Create your models here.


class UserAccount(models.Model):
    CodeName = models.CharField('CodeName', max_length=30, primary_key=True)
    Password = models.CharField('Password', max_length=20, null=False)
    Permission = models.PositiveSmallIntegerField('Permission', null=False)
    Mail = models.CharField('Mail', max_length=20, default="")

    class Meta:
        db_table = 'user_account'

    def __str__(self):
        return self.CodeName


class UserProfile(models.Model):
    # OId = models.AutoField('OId', primary_key=True)

    CodeName = models.CharField('CodeName', max_length=30, primary_key=True)
    Gender = models.IntegerField('Gender', choices=((0, 'male'), (1, 'female')))  # 0表示男性，1表示女性
    Class = models.CharField('Class', max_length=20)
    Region = models.CharField('Region', max_length=30)
    Race = models.CharField('Race', max_length=20)
    Avatar = models.ImageField(verbose_name='Avatar', upload_to='img_url', null=True)
    Bio = models.TextField('Bio', default="")

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.CodeName


class AccountApproveQueue(models.Model):
    # OId = models.AutoField('OId', primary_key=True)
    CodeName = models.CharField('CodeName', max_length=30, primary_key=True)
    Password = models.CharField('Password', max_length=20, null=False)
    Permission = models.IntegerField('Permission', null=False, default=3)
    Class = models.CharField('Class', max_length=20)
    Region = models.CharField('Region', max_length=30)
    Race = models.CharField('Race', max_length=20)
    Description = models.TextField('Description', default="")

    class Meta:
        db_table = 'account_approve_queue'

    def __str__(self):
        return self.CodeName


class Passage(models.Model):
    PId = models.AutoField('PId', primary_key=True)
    Title = models.CharField('Title', max_length=45, null=False)
    Poster = models.CharField('Poster', max_length=30, null=False)
    PostDate = models.DateTimeField('PostDate', default=datetime.datetime.now, null=False)
    LastEditor = models.CharField('LastEditor', max_length=30, null=False)
    LastEditTime = models.DateTimeField('LastEditTime', auto_now=True, null=False)
    Content = models.TextField('Content', null=False)
    Type = models.IntegerField('Type', null=False, default=1)

    class Meta:
        db_table = 'passage'
        ordering = ['-LastEditTime']

    def __str__(self):
        return str(self.PId)


class Group(models.Model):
    Gid = models.AutoField('GId', primary_key=True)
    GName = models.CharField('GName', max_length=30)
    Owner = models.ForeignKey(UserAccount, null=False, on_delete=models.CASCADE)
    BornTime = models.DateTimeField('Time', auto_now=True, null=False)

    class Meta:
        db_table = 'Group'

    def __str__(self):
        return str(self.Gid)


class Message(models.Model):
    MId = models.AutoField('MId', primary_key=True)
    Type = models.IntegerField('Type', choices=((0, '个人'), (1, '群组')))
    SendFrom = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='SendFrom')
    SendToPerson = models.ForeignKey(UserAccount, null=True, on_delete=models.CASCADE, related_name='SendToPerson')
    SendToGroup = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    ContextText = models.TextField('ContextText')
    Picture = models.ImageField(verbose_name='Picture', upload_to='img_url', null=True)
    Time = models.DateTimeField('Time', auto_now=True, null=False)

    class Meta:
        db_table = 'Message'

    def __str__(self):
        return str(self.MId)


class OperatorGroup(models.Model):
    Gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    CodeName = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    isOwner = models.IntegerField('isOwner', choices=((0, '不是'), (1, '是')))

    class Meta:
        db_table = 'operator_group'
        unique_together = ('Gid', 'CodeName')

    def __str__(self):
        return str(self.Gid) + str(self.CodeName)


class Reply(models.Model):
    RId = models.AutoField('RId', primary_key=True)
    Replier = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    AttachedPId = models.ForeignKey(Passage, on_delete=models.CASCADE)
    Content = models.TextField("Content")

    class Meta:
        db_table = 'Reply'

    def __str__(self):
        return str(self.RId)
