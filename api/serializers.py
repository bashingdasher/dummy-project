from rest_framework import serializers
from todolist.models import Task
from django.contrib.auth.models import User

class taskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status"]
        ordering = ["-updated"]

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]