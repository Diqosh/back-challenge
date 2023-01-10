from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from challenge.models import CustomUser, Company
from challenge.serializer import CustomUserSerializer, CompanySerializer


@extend_schema(methods=['GET', 'POST'], request=CustomUserSerializer, responses=CustomUserSerializer)
@api_view(('GET', 'POST'))
def user_list(request):
    if request.method == "GET":
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


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
