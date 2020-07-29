from django.urls import path
from .views import CustomUserCreate, CustomUserDetail, TeacherList, StudentList, ClassroomList, TeacherDetail, StudentDetail, ClassroomDetail, ObtainTokenPairView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/obtain/', ObtainTokenPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:user_id>', CustomUserDetail.as_view()),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:teacher_id>/edit', TeacherDetail.as_view()),
    path('students/', StudentList.as_view()),
    path('students/<int:student_id>/edit/', StudentDetail.as_view()),
    path('classes/', ClassroomList.as_view()),
    path('classes/<int:class_id>/edit/', ClassroomDetail.as_view()),
]