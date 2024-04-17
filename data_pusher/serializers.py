# serializers.py
from rest_framework import serializers
from .models import Account, Destination
import secrets

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'url', 'http_method', 'headers']

from rest_framework import serializers
from .models import Account
import secrets

class AccountSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, read_only=True)
    app_secret_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'email', 'account_id', 'account_name', 'website', 'app_secret_token', 'destinations']
        read_only_fields = ['id', 'app_secret_token']

    def create(self, validated_data):
        if 'app_secret_token' not in validated_data:
            validated_data['app_secret_token'] = secrets.token_urlsafe(32)

        if 'account_id' in validated_data and Account.objects.filter(account_id=validated_data['account_id']).exists():
            raise serializers.ValidationError({'account_id': 'This account ID already exists.'})

        account = Account.objects.create(**validated_data)
        account.save()
        
        return account
