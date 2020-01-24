from rest_framework import serializers

from .models import People

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = [
            'id', 'first_name', 'last_name', 'nickname', 'favorite_color', 'birth_date', 'created_at', 'author'
        ]

