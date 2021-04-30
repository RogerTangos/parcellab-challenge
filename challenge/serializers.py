from rest_framework import serializers

from .models import Tracking, Checkpoint


class CheckpointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checkpoint
        fields = ['location',
                  'timestamp', 'status', 'status_text',
                  'status_details']


class TrackingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tracking
        fields = ['orderNo', 'tracking_number', 'courier', 'street', 'zip_code', 'city',
                  'destination_country_iso3', 'email', 'articleNo', 'articleImageUrl',
                  'quantity', 'product_name']
