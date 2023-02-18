from rest_framework import serializers

from .models import Cards

class CardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'
