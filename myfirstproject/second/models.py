# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User_custom(models.Model):
    pseudo = models.CharField(max_length=20)
    mdp = models.CharField(max_length=20)
