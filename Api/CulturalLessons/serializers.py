from rest_framework import serializers
from .models import CulturalLesson, UserCulturalLesson

class CulturalLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalLesson
        fields = '__all__'

class UserCulturalLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCulturalLesson
        fields = '__all__'
