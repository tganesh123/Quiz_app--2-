from django.urls import path
from . import views
urlpatterns = [
    path('' , views.quizApp, name="quizApp"),
    path('api/get-quiz/', views.get_quiz , name="get_quiz"),
    path('quiz/' , views.quiz, name="quiz")
]
