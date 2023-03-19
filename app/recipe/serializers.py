"""
Serializers for recipe APIs
"""
from rest_framework import serializers
from core.models import Recipe

from django.utils.translation import gettext as _


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""

    class Meta:
        model = Recipe
        fields = ['ide', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
