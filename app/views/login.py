from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime, timedelta
import jwt
import json

token_key = "SamUelhjihdjighjidhjsshjdf4df56b456dsdnvjbddjdb1d651b5dbvnjshgHVHHjidgd4df54dnhjBHBhjbjkndkn"



def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).values()
        print("USER_DATA : ", user)
        if user:
            user = list(user)
            datauser = {"id" : user[0].get('id'), "username":user[0].get('username'), "exp": (datetime.now() + timedelta(days=3)).timestamp()}
            token = jwt.encode(datauser, token_key, algorithm='HS256')
            response = HttpResponse(
                render(
                    request, 
                    'app/home/index.html', 
                    {
                        "username": user[0].get('username')
                    }
                )
            )
            response.set_cookie('jwt', token)
            return response
        else:
            messages.error(request, 'Les informations fournies ne sont pas correctes.')