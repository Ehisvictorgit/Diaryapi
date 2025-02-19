from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializers):
    class Meta:
        model = Diary
        fields = '__all__'
        