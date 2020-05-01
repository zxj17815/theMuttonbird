#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :models.py
@Description :
@DateTiem    :2020-05-01 15:40:41
@Author      :Jay Zhang
'''
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        null=True,
        help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    password = models.CharField('password', max_length=128,blank=True)

    # objects = UserManager()

    # USERNAME_FIELD='uid'
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)