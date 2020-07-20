from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.linkedin.views import *
from allauth.socialaccount.providers.linkedin_oauth2.views import *
from .serializers import UserCreateSerializer
# Create your views here.

User = get_user_model()

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)


class LinkedinLogin(SocialLoginView):
    adapter_class = LinkedInOAuth2Adapter