from django.db import models


# Create your models here.


class UserAccount(models.Model):
    OId = models.AutoField('OId', primary_key=True)
    CodeName = models.CharField('CodeName', max_length=30)
    Password = models.CharField('Password', max_length=20, null=False)
    Permission = models.PositiveSmallIntegerField('Permission', null=False)
    Mail = models.CharField('Mail', max_length=20)

    class Meta:
        db_table = 'user_account'

    def __str__(self):
        return self.CodeName


class UserProfile(models.Model):
    OId = models.AutoField('OId', primary_key=True)
    CodeName = models.CharField('CodeName', max_length=30)
    Gender = models.IntegerField('Gender', choices=((0, 'male'), (1, 'female')))  # 0表示男性，1表示女性
    Class = models.CharField('Class', max_length=20)
    Region = models.CharField('Region', max_length=30)
    Race = models.CharField('Race', max_length=20)
    Avatar = models.ImageField('Avatar', null=True)
    Bio = models.TextField('Bio')

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.CodeName


class AccountApproveQueue(models.Model):
    OId = models.AutoField('OId', primary_key=True)
    CodeName = models.CharField('CodeName', max_length=30)
    Password = models.CharField('Password', max_length=20, null=False)
    Permission = models.IntegerField('Permission', null=False,default=3)
    Class = models.CharField('Class', max_length=20)
    Region = models.CharField('Region', max_length=30)
    Race = models.CharField('Race', max_length=20)
    Description = models.TextField('Description')

    class Meta:
        db_table = 'account_approve_queue'

    def __str__(self):
        return self.CodeName
