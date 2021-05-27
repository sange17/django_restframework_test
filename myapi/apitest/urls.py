# 이 앱에 대한 url들을 관리한다.
from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/",helloAPI),
    path("<int:id>/",randomQuiz)
]
