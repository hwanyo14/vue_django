from django.db import models

# Create your models here.
class Todo(models.Model):   # 테이블 모델 생성
  name = models.CharField('NAME', max_length=5, blank=True)   # attribute column
  todo = models.CharField('TODO', max_length=50)

  def __str__(self):
    return self.todo

  def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    if not self.name:
      self.name = '홍길동'
    super().save()