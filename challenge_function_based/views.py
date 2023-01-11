from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from challenge.models import CustomUser, Company
from challenge.serializer import CustomUserSerializer, CompanySerializer, RegistrationSerializer


@extend_schema(methods=['GET', ], responses=CustomUserSerializer)
@api_view(('GET', ))
def user_list(request):
    if request.method == "GET":
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


@extend_schema(methods=['GET', 'POST'], request=RegistrationSerializer, responses=RegistrationSerializer)
@api_view(('POST',))
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            data['birth_date'] = account.birth_date
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
        else:
            data = serializer.errors
        return Response(data)


@api_view(('GET',))
def user_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


@extend_schema(methods=['POST'], request=CompanySerializer, responses=CompanySerializer)
@api_view(('GET', 'POST'))
def company_list(request):
    if request.method == "GET":
        users = Company.objects.all()
        serializer = CompanySerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(('GET', 'PUT', 'DELETE'))
def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        company.delete()
        return Response(status=204)
