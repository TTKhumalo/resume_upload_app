from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("upload_resume/", views.upload_resume, name="upload_resume"),
    path("view_resume/", views.view_resume, name="view_resume"),
    path("admin_view_users/", views.admin_view_users, name="admin_view_users"),
    path(
        "view_user_resumes/<int:user_id>/",
        views.view_user_resumes,
        name="view_user_resumes",
    ),
    path("profile/", views.profile, name="profile"),
]
