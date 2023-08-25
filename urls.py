#go to urls.py in mysite project
from django.contrib import admin
from django.urls import path
from app import views # importing views file in app folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index ,name="index") # calling function named index from views file
]
#then give python manage.py runserver in cmd prompt in mysite project location
