"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', cars_view, name='cars_list'),
    path('new_car/', new_car_view, name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)