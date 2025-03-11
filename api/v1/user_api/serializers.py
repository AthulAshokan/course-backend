from rest_framework import serializers
from users.models import CustomUser

from django.contrib.auth import authenticate

# register serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email_or_username = data.get('email_or_username')
        password = data.get('password')

        user = None
        # Check if input is email or username
        if '@' in email_or_username:
            user = CustomUser.objects.filter(email=email_or_username).first()
        else:
            user = CustomUser.objects.filter(username=email_or_username).first()

        # Authenticate user
        if user and user.check_password(password):
            if not user.is_active:
                raise serializers.ValidationError("User account is not active.")
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Invalid credentials.")



  

       

