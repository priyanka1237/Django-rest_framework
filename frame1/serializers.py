from rest_framework import serializers
from frame1.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('created', 'title', 'code', 'linenos', 'language', 'style')