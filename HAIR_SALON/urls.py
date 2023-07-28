"""HAIR_SALON URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('scheduler', views.FreeSlots.as_view(), name="FreeSlots"),
    path('appointments', views.Appointments.as_view(), name="appointments"),
    path('accounts', include('allauth.urls')),
    path('edit/<item_id>', views.edit_appointments, name="edit_appointments"),
    path('delete/<item_id>', views.delete_appointments, name="delete_appointments"),
]

# Custom error views for 404 Not Found and 500 Server Error
handler404 = views.handler404
handler500 = views.handler500
