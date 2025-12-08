from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    CATEGORY = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()

    # ✅ এই দুইটা এখন NULL হতে পারবে (এটাই মূল Fix)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=STATUS, default='Pending')
    category = models.CharField(max_length=10, choices=CATEGORY)
    is_completed = models.BooleanField(default=False)

    # ✅ USER এখন OPTIONAL
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
