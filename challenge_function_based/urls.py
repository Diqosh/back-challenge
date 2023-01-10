from django.urls import path

from challenge_function_based.views import user_list, user_detail, company_list, company_detail

# 1 means function based views
urlpatterns = [
    path('users/', user_list),
    path('users/<int:pk>', user_detail),
    path('companies/', company_list),
    path('companies/<int:pk>', company_detail),
]
