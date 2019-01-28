from django.forms import ModelForm, TextInput
from .models import hashtag, task

class AddCategory(ModelForm):
    class Meta:
        model = hashtag
        fields = ['category']
        # widgets = {
        #     'category': TextInput(attrs={'class': 'input', 'placeholder': 'Enter the category name'}),
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].widget.attrs['class'] = 'input'

class AddTask(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'hashtag', 'schedule_time_to_start', 'deadline', 'priority']
