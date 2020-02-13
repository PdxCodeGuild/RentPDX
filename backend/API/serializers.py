from rest_framework import serializers
from django.contrib.auth.models import User
from Home.models import Home

# User Serializer Here


# Home serializer
class HomeSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(read_only=True)

    class Meta:
        model = Home
        fields = (
            'id',
            'user',
            'user_info',
            'street_addr',
            'zip_code',
            'max_occupancy',
            'housing_type',
            'rent_amt',
            'sq_ft',
            'no_bdr',
            'no_bath',
            'pkg_type',
            'term_mo',
            'ada',
            'pets',
            'furnished',
            'smoking',
            'no_app_fee',
            'no_broker_fee',
            'img'
        )
