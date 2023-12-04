from rest_framework import serializers
from .models import Message, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "name", "userlist")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "room", "user", "content", "timestamp")
        read_only_fields = ("id", "timestamp")
