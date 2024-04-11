from rest_framework import serializers

class EventUrlSerializer(serializers.ModelSerializer):
    source_url = serializers.CharField(max_length = 100)
    event_url = serializers.CharField(max_length = 100)

