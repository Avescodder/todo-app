from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Task


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    """
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user data
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
        read_only_fields = ('id', 'date_joined')


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'completed', 
            'priority', 'created_at', 'updated_at', 'user'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')

    def validate_title(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Заголовок должен содержать минимум 2 символа")
        return value.strip()

    def validate_description(self, value):
        if value and len(value.strip()) > 1000:
            raise serializers.ValidationError("Описание не должно превышать 1000 символов")
        return value.strip() if value else ""


class TaskCreateUpdateSerializer(TaskSerializer):
    """
    Serializer for creating and updating tasks
    """
    class Meta(TaskSerializer.Meta):
        fields = ['title', 'description', 'completed', 'priority']