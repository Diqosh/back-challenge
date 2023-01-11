from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from .models import CustomUser, Company, Feedback
from datetime import datetime


def getAge(birth_date):
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    birthYear, birthMonth, birthDay = str(birth_date).split('-')
    return ((currentYear - int(birthYear)) * 365 + (currentMonth - int(birthMonth)) * 30 + (
            currentDay - int(birthDay))) // 365


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'birth_date')

    def create(self, validated_data):
        """
        Create and return a new `Company` instance, given the validated data.
        """
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Company` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()

        return instance

    def validate(self, attrs):
        age = getAge(attrs['birth_date'])
        if not attrs['birth_date']:
            raise serializers.ValidationError("there is must be a birth date")
        if age < 16:
            raise serializers.ValidationError("ебалай расти давай")
        return attrs


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Company` instance, given the validated data.
        """
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Company` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.company_type = validated_data.get('company_type', instance.company_type)
        instance.date_creation = validated_data.get('date_creation', instance.date_creation)
        instance.date_update = validated_data.get('date_update', instance.date_update)
        instance.save()

        return instance

    def validate(self, attrs):
        attrs1 = super().validate(attrs)
        errors = {}

        # if attrs['time_start'] >= attrs['time_end']:
        #     errors['time_start'] = ['незя']

        if errors:
            raise errors

        return attrs


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'text', 'star', 'author', 'company')
