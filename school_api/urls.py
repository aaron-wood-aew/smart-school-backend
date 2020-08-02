from django.urls import path
from .views import CustomUserCreate, CustomUserDetail, TeacherList, StudentList, ClassroomList, TeacherDetail, StudentDetail, ClassroomDetail, StudentCreate, ClassroomCreate, Login


urlpatterns = [

    path('user/<int:pk>', CustomUserDetail.as_view()),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('login/', Login.as_view()),
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:teacher_id>/edit', TeacherDetail.as_view()),
    path('user/<int:user_id>/students/', StudentList.as_view()),
    path('user/<int:user_id>/students/create/', StudentCreate.as_view(), name="create_student"),
    path('user/<int:user_id>/students/<int:student_id>/', StudentDetail.as_view()),
    path('classes/', ClassroomList.as_view()),
    # path('classes/create/', ClassroomCreate.as_view(), name="create_classroom"),
    path('classes/<int:pk>/', ClassroomDetail.as_view()),
]