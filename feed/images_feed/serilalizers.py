from django.core.files.storage import FileSystemStorage
from rest_framework import serializers

from feed_exceptions.feed_exceptions import InvalidAPIQuery

# from feed import settings
#
# fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class FeedListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    status = serializers.BooleanField()



