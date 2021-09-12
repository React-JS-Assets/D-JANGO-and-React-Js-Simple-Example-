from rest_framework import serializers
from .models import Todo, user


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["username",
                  "first_name",
                  "last_name",
                  "phone_number",
                  "email",
                  ]

    def create(self, validated_data):
        # Once the request data has been validated, we can create a todo item instance in the database
        return user.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone_number=validated_data.get('phone_number'),
        )
