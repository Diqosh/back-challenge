from django.urls import path
from .views import current_datetime, CustomUserList, CompanyList, FeedbackList, user_list, user_detail, company_list, company_detail

# 1 means function based views
urlpatterns = [
    path('test/', current_datetime),
    path('users/', CustomUserList.as_view()),
    path('users1/', user_list),
    path('users/<int:pk>', user_detail),
    path('companies/', CompanyList.as_view()),
    path('companies1/', company_list),
    path('companies1/<int:pk>', company_detail),

    path('feedbacks/', FeedbackList.as_view()),
]
