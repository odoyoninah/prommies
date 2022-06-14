from rest_framework import serializers
from .models import Prommies, Profile

class PrommiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prommies
        fields = ('name', 'description', 'score', 'image', 'email', 'url')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image', 'bio', 'birth_date', 'mobile', 'project')