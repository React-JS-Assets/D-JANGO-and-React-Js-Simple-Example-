from django.http import response
from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Todo, user
import json
from .serializer import TodoSerializer, UserSerializer
# Create your views here.


@api_view(['GET'])
def index(request):
    todos = Todo.objects.all()
    print("this is ", todos)
    serializer = TodoSerializer(todos, many=True)
    # print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def loginUser(request):
    if request.method == "POST":
        data = (request.data)
        print(data.get('password'))
        print(data.get('username'))

        # Attempt to sign user in
        password = data.get('password')
        username = data.get('username')

        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return Response({"message": "login success"}, 200)
        else:
            return Response({
                "message": "Invalid username and/or password."
            }, 201)

    else:
        return Response({"message": "eTesting/login.html"}, 401)


sample = {
    "username": "ahsan12345",
    "first_name": "ahsan",
    "last_name": "ansari",
    "phone_number": "0789768",
    "password": "ahsan131",
    "email": "ahsanayan131@gmail.com"

}
sample3 = {
    "username": "ahsan12345",
    "password": "ahsan131",

}


@api_view(['GET'])
def logoutUser(request):
    logout(request)
    return Response({"message": "succes fully logout"}, 200)


@ api_view(['POST'])
def register(request):
    if request.method == "POST":
        # userdata = json.loads(request.data)
        print(request.data)
        data = request.data
        # Attempt to create new user
        try:
            newuser = user.objects.create_user(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                phone_number=data.get('phone_number'))
            newuser.save()
        except IntegrityError:
            print(ImportError.msg)
            return Response({
                "message": "Username already taken."
            }, 401)
        login(request, newuser)
        return Response({
            "message": "successfully created user"
        }, 200)
    else:
        return Response({
            "message": "retry later"
        }, 401)
