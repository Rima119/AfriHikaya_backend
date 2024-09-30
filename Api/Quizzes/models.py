from django.db import models
from django.contrib.auth import get_user_model
from CulturalLessons.models import *
# Create your models here.

class Quiz(TimestampedModel):
    cultural_lesson = models.ForeignKey(CulturalLesson, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    time_duration = models.IntegerField()  # durée en minutes

    def __str__(self):
        return self.title

class UserQuiz(TimestampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"

class Question(TimestampedModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.question_text