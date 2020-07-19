from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
# Create your views here.
class Home(APIView):
     def get(self, request, format=None):
         data = {"status":"OK"}
         return Response(data)

class CategoryList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ConfOwnProfileList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = ConfOwnProfile.objects.all()
    serializer_class = ConfOwnProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConfOwnProfileDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return ConfOwnProfile.objects.get(pk=pk)
        except ConfOwnProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ConfOwnProfileSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ConfOwnProfileSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConferenceList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        print("conference create", kwargs, request)
        return self.create(request, *args, **kwargs)

class ConferenceDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Conference.objects.get(pk=pk)
        except Conference.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ConferenceSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ConferenceSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LocationList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LocationDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LocationSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LocationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RatingList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RatingDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RatingSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RatingSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ReportList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReportDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReportSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReportSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SpeakerList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SpeakerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Speaker.objects.get(pk=pk)
        except Speaker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SpeakerSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SpeakerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClaimList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

    def get(self, request, *args, **kwargs):
        print("hello")
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClaimDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Claim.objects.get(pk=pk)
        except Claim.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ClaimSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ClaimSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)