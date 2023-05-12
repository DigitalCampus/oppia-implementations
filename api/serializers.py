from rest_framework import serializers

from oppia_implementations.models import OppiaImplementation


class OppiaImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OppiaImplementation
        fields = ['title', 'url']
