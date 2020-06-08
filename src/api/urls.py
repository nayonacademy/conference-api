from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('status', Home.as_view(), name="api"),
    path('category/list/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('confprofile/list/', ConfOwnProfileList.as_view()),
    path('confprofile/<int:pk>/', ConfOwnProfileDetail.as_view()),
    path('conference/list/', ConferenceList.as_view()),
    path('conference/<int:pk>/', ConferenceDetail.as_view()),
    path('location/list/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('rating/list/', RatingList.as_view()),
    path('rating/<int:pk>/', RatingDetail.as_view()),
    path('report/list/', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view()),
    path('speaker/list/', SpeakerList.as_view()),
    path('speaker/<int:pk>/', SpeakerDetail.as_view()),
    path('claim/list/', ClaimList.as_view()),
    path('claim/<int:pk>/', ClaimDetail.as_view()),
]