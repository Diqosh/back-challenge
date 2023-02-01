from rest_framework import serializers, authentication
from .models import CustomUser, Company, Feedback
from datetime import datetime

def get_age(birth_date: datetime.date) -> int:
    diff = datetime.now().date() - birth_date
    return diff.days // 365


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_birth_date(self, birth_date):
        if get_age(birth_date) < 16:
            raise serializers.ValidationError("ебалай расти давай")
        return birth_date


class RegistrationSerializer(CustomUserSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'password', 'password2', 'first_name', 'last_name', 'birth_date')

    def save(self):
        user = CustomUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='author', write_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company', write_only=True)
    author = serializers.CharField(source='author.username', read_only=True)
    company = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'

    def validate(self, data):
        print(self.context)
        feedbacks = Feedback.objects.filter(author=self.context['request'].user, company=data['company'])
        if len(feedbacks) > 1:
            raise serializers.ValidationError("no one more feedback")
        return data

