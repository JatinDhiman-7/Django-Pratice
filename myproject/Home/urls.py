from django.urls import path
from Home import views
urlpatterns=[
    path("",views.index,name='Home'),
    path("about/",views.about,name='about'),
    path("services/",views.services,name='service'),
    path("contact/",views.contact,name='contact'),
]