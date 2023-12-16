from rest_framework import serializers
from .models import Train, Seats
from django.contrib.auth.models import User

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_category(self, value):

        if not Train.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Обраного поїзду не існує.")
        return value

class AdminLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)