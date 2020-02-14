from rest_framework import serializers
from users.models import CustomUser
from Home.models import Home

# User Serializer Here
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'user_type',
            'birthdate',
        )

# Home serializer
class HomeSerializer(serializers.ModelSerializer):
    user_info = CustomUserSerializer(read_only=True)

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

