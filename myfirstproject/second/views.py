# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import User_custom
from .forms import UserForm

from django.http import HttpResponseRedirect
from django.utils.html import escape

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def second_view(request):

    form = UserForm()

    if request.method == "POST":
        #form = PostStoryForm(request.POST)
        #if form.is_valid():
        #    obj = form.save(commit=False)
        #    obj.author = request.user
        #    new_post = obj.save()
        #    print(new_post)

        # if form.is_valid():
            #userform = User_custom(request.POST)
            user = User_custom()
            user.pseudo = request.POST['pseudo']
            user.mdp = request.POST['mdp']
            user.save()
            return redirect(second_view)

    else:
        users = User_custom.objects.all()


    return render(request, 'second_view.html', {'form': form, 'users': users})




    #>> > f = ArticleForm(request.POST)

    # Save a new Article object from the form's data.
    #>> > new_article = f.save()

    # Create a form to edit an existing Article, but use
    # POST data to populate the form.
    #>> > a = Article.objects.get(pk=1)
    #>> > f = ArticleForm(request.POST, instance=a)
    #>> > f.save()