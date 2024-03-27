from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('form/',views.submit_form),
    path("django/",views.DjangoForm,name='django'),
]
