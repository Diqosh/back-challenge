from django.urls import path
from .views import current_datetime, CustomUserList, CompanyList, FeedbackList

urlpatterns = [
    path('test/', current_datetime),
    path('users/', CustomUserList.as_view()),

    path('companies/', CompanyList.as_view()),

    path('feedbacks/', FeedbackList.as_view()),
]
