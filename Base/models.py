#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File        :models.py
@Description :
@DateTiem    :2020-05-01 15:40:41
@Author      :Jay Zhang
"""
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
import uuid


# Validators
@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    """PhoneNumber Validator (Just China Mobile)"""
    regex = r'^1[3,4,5,6,7,8]\d{9}$'
    message = _(
        'Enter a valid Phone Number. This value may contain only numbers. '
    )
    flags = 0


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField('Id', primary_key=True, auto_created=True, default=uuid.uuid4,
                          editable=False, help_text="string(150),唯一ID")
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
    phone_number = models.CharField(
        'phone_number',
        max_length=18,
        unique=True,
        null=True,
        help_text='11 characters, only numbers',
        validators=[PhoneNumberValidator],
        error_messages={
            'unique': "A user with that phone_number already exists.",
        }
    )
    password = models.CharField('password', max_length=128, blank=True)

    # objects = UserManager()

    # USERNAME_FIELD='uid'
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)
