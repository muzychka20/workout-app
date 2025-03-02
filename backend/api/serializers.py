from api.models import User, Goal, TrainingType, Sex, BodyType, PhysicalLevel
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    # goal = serializers.StringRelatedField()
    # body_type = serializers.StringRelatedField()
    # sex = serializers.StringRelatedField()
    # physical_level = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "goal", "body_type", "sex", "physical_level", "registered_time", "age", "weight", "height"
        ]

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        errors = []

        # username validation
        if User.objects.filter(username=username).exists():
            errors.append("A user with this username already exists")
        if len(username) < 4:
            errors.append("username must be at least 4 characters long")

        # password validation
        if len(password) < 8:
            errors.append("password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            errors.append("password must contain at least one numeric digit")
        if not any(char.isupper() for char in password):
            errors.append(
                "password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            errors.append(
                "password must contain at least one lowercase letter")
        if confirm_password != password:
            errors.append("passwords are not the same!")

        if errors:
            raise serializers.ValidationError({"detail": {"errors": errors}})

        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        errors = []

        if not User.objects.filter(email=email).exists():
            errors.append("User with this email does not exist")
        else:
            user = authenticate(email=email, password=password)
            if user is None:
                errors.append("Incorrect password")

        if errors:
            raise serializers.ValidationError({"detail": {"errors": errors}})

        return {'user': user}


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            "id", "name"
        ]


class PhysicalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalLevel
        fields = [
            "id", "name"
        ]


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = [
            "id", "name"
        ]


class SexTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = [
            "id", "name"
        ]


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = [
            "id", "name", "duration_sec", "duration_name"
        ]
