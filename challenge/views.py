from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics, serializers
from rest_framework.response import Response
from challenge.models import CustomUser, Company, Feedback
from challenge.serializer import CustomUserSerializer, CompanySerializer, FeedbackSerializer
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_type']


@extend_schema(methods=['POST'], responses=FeedbackSerializer)
class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['star', 'author', 'company']

    def create(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=201)




