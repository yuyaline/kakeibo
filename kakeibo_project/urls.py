from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ←これを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kakeibo.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ←これを追加
]