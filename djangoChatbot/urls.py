"""djangoChatbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from chatbot import views as chatbot_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', chatbot_views.call_model.as_view(),name='predict'),
    path('translate/', chatbot_views.translate.as_view(),name='translate'),
    path('listen/', chatbot_views.listen.as_view(),name='listen'),
    path('speak/', chatbot_views.speak.as_view(),name='speak'),
     path('explore/', chatbot_views.explore.as_view(),name='explore'),
]
