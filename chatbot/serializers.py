from rest_framework import serializers

from .models import CancerImage


class CancerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancerImage
        fields = ('id', 'image',)

    def create(self, validated_data):
        return CancerImage.objects.create(**validated_data)