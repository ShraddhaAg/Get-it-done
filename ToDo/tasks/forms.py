from django.forms import ModelForm
from .models import hashtag, task

class AddCategory(ModelForm):
    class Meta:
        model = hashtag
        fields = ['category']

class AddTask(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'hashtag', 'schedule_time_to_start', 'deadline', 'priority']
