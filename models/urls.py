from django.urls import path
from .views import *

urlpatterns = [
    path('contact-us/', ContactCreateView.as_view()),
    path('contacts/', AllContactView.as_view()),
    path('called-contact/', CalledContactView.as_view()),
    path('uncalled-contact/', UnCalledContactView.as_view()),
    path('contact/<pk>/', ContactDetailView.as_view()),
]