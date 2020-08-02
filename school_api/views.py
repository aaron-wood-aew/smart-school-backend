from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, Student, Teacher, Address, Classroom, Account
from .serializers import StudentSerializer, TeacherSerializer, ClassroomSerializer, CustomUserSerializer, LoginSerializer, ParentSerializer, AddressSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print("Successful!)")
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, user_id, format='json'):
        serializer = StudentSerializer(data=request.data)
        user_id = User.objects.get(id=user_id)
        if serializer.is_valid():
            serializer.save()
            json = serializer.data
            return Response(json, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, user_id, *args, **kwargs):
        user_id = User.objects.get(id=user_id)
        student_id = self.get_object()
        serializer = StudentSerializer(student_id)
        return Response(serializer.data)
    
    def delete(self, request, user_id, format='json'):
        serializer = StudentSerializer(data=request.data)
        user_id = User.objects.get(id=user_id)
        if serializer.is_valid():
            # user = serializer.save() ... pass instance / use .delete
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomCreate(generics.CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class ClassroomList(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=False)
    #     import pdb; pdb.set_trace()
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, validated_data):
    #     address = validated_data.pop('address')
    #     classroom = Classroom.objects.create(**validated_data)
    #     address_object = Address.objects.create(**address)
    #     return classroom

class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

def _google_address(address):
    modified_address = address.replace(' ', '+')
    return f"https://www.google.com/maps/embed/v1/place?q={modified_address}&key={settings.GOOGLE_MAPS_API_KEY}"
    