from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from .models import CustomUser, Student, Teacher, Address, Classroom, Account, Parent

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password',
            'is_teacher',
            'is_guardian',
        ]

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password',
        ]
    """
    Currently unused in preference of the below.
    """
    # email = serializers.EmailField(
    #     required=True
    # )
    # password = serializers.CharField(min_length=8, write_only=True)

    # class Meta:
    #     model = CustomUser
    #     fields = [
    #         'email',
    #         'password']

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'parent_id',
            'first_name',
            'last_name',
            'grade',
        ]

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = [
            'user_id',
            'address',
        ]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'user_id',
            'grade',
            'rate',
        ]

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'street_1',
            'street_2',
            'city',
            'state',
            'zip_code',
        ]

class ClassroomSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Classroom
        fields = [
            'name',
            'address',
            'teacher',
            'start_date',
            'end_date',
        ]

    def create(self, validated_data):
        address = validated_data.pop('address')
        classroom = Classroom(**validated_data)
        address_object = Address.objects.create(**address)
        classroom.address = address_object
        classroom.save()
        return classroom

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        instance.name = validated_data.get('name', instance.name)
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        address.street_1 = address_data.get('street_1', address.street_1)
        address.street_2 = address_data.get('street_2', address.street_2)
        address.city = address_data.get('city', address.city)
        address.state = address_data.get('state', address.state)
        address.zip_code = address_data.get('zip_code', address.zip_code)
        address.save()
        return instance