from rest_framework import serializers

from social.constants import ANALYTICS_TYPES


class DateSerializer(serializers.Serializer):
    date_from = serializers.DateField(format='%d-%m-%Y')
    date_to = serializers.DateField(format='%d-%m-%Y')
    aggregate_by = serializers.ChoiceField(choices=ANALYTICS_TYPES, required=False)
