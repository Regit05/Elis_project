# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import User
from .forms import UserForm


# Create your views here.

def second_view(request):
    user = User()
    form = UserForm()

    return render(request, 'second_view.html', {'user': user, 'form':form})