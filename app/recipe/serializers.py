"""
serializers for recipe API
"""
from rest_framework import serializers

from core.models import Recipie

class RecipeSerializer(serializers.ModelSerializer):
  """Serializers for recipes."""

  class Meta:
    model=Recipie
    fields=['id','title','time_minutes', 'price','link']
    read_only_fields=['id']

class RecipeDetailSerializer(RecipeSerializer):
  """serializer for recipe detail view"""
  class Meta(RecipeSerializer.Meta):
    fields=RecipeSerializer.Meta.fields + ['description']
    
