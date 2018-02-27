# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def second_view(request):
    return render(request, 'second_view.html', {})