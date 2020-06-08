from django.contrib.auth.models import User, Group
from api.models import *
from rest_framework import serializers


# class AdSizesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdSizes
#         fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # depth = 1
        fields = '__all__'

class ConfOwnProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ConfOwnProfile
        # depth = 1
        fields = '__all__'

class ConferenceSerializer (serializers.ModelSerializer):
    class Meta:
        model = Conference
        # depth = 1
        fields = '__all__'

class LocationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Location
        # depth = 1
        fields = '__all__'

class RatingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rating
        # depth = 1
        fields = '__all__'

class ReportSerializer (serializers.ModelSerializer):
    class Meta:
        model = Report
        # depth = 1
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        # depth = 1
        fields = '__all__'

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        # depth = 1
        fields = '__all__'