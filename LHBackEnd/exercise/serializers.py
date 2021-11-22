from userprofile.models import User
from rest_framework import serializers

from .models import Courses


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'email',)


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(required=False)

    class Meta:
        model = Courses
        fields = '__all__'

    def update(self, instance, validated_data):
        print(validated_data)
        pass

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        course = Courses.objects.create(**validated_data)
        course.teacher = user
        course.save()
        return course