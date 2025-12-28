from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'due_date',
            'due_time',
            'status',
            'category',
        ]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "due_time": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
        }

    # (Optional but helpful) to accept both HH:MM and HH:MM:SS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["due_time"].input_formats = ["%H:%M", "%H:%M:%S"]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']






        
