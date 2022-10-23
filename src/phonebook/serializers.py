from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        name = validated_data.get('name')
        return Person.objects.create(name=name)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
