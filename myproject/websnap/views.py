from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.models import User


from .models import *

def index(request):
    data = None  # Initialize 'data' with a default value

    if request.method == "POST":
        # Attempt to create a Messages object
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        messages = request.POST["messages"]
        
        data = Messages.objects.create(
            firstname=firstname, 
            lastname=lastname, 
            email=email, 
            phonenumber=phonenumber, 
            messages=messages
        )
        
    return render(request, 'index.html', {'data': data})



    
    #     # Check if authentication successful
    #     if user is not None:
    #         # login(request, user)
    #         return redirect('index')
    #     else:
    #         return render(request, "login.html", {
    #             "message": "Invalid username and/or password."
    #         })
    # else:
    #     return render (request, "login.html")


