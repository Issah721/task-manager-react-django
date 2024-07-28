from rest_framework import serializers
from .models import Todo # type: ignore

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')