from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('status', Home.as_view(), name="api"),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('confprofile/', ConfOwnProfileList.as_view()),
    path('confprofile/<int:pk>/', ConfOwnProfileDetail.as_view()),
    path('conference/', ConferenceList.as_view()),
    path('conference/<int:pk>/', ConferenceDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('rating/', RatingList.as_view()),
    path('rating/<int:pk>/', RatingDetail.as_view()),
    path('report/', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view()),
    path('speaker/', SpeakerList.as_view()),
    path('speaker/<int:pk>/', SpeakerDetail.as_view()),
    path('claim/', ClaimList.as_view()),
    path('claim/<int:pk>/', ClaimDetail.as_view()),
]