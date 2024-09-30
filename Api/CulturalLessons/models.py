from django.db import models
from django.contrib.auth import get_user_model


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CulturalLesson(TimestampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.title

class UserCulturalLesson(TimestampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='cultural_lessons')
    cultural_lesson = models.ForeignKey(CulturalLesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.cultural_lesson.title}"
