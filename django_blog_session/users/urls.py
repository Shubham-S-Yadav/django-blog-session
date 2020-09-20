from django.conf.urls import url
from .views import HelloWorld, HelloWorldTwo

urlpatterns = [
    url('our_first_api', HelloWorld.as_view()),
    url('our_second_api', HelloWorldTwo.as_view()),
]