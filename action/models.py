from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=256)
    problem = models.TextField()
    description = models.TextField(blank=True)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
