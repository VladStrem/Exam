from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    # path("login/", views.user_login, name="login"),
    path("login/", views.LoginUser.as_view(), name="login"),
    # path("logout/", views.user_logout, name="logout"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logged_out.html"), name="logout"),
    path("profile/", views.dashboard, name="dashboard"),

    path("register/", views.UserRegisterView.as_view(), name="register"),

    path('password/change/', views.CustomPasswordChangeView.as_view(), name='password-change'),
    path('password/change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password-change-done'),

    path("profile/edit/", views.edit_profile, name="profile-edit"),
    # path("profile/edit/", views.ProfileUpdateView.as_view(), name="profile-edit"),
]
