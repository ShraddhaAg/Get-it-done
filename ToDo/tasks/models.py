from django.db import models

class hashtag(models.Model):

    category = models.CharField(max_length=20, help_text='Enter a new category of tasks!')
    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        ordering = ['category']

class task(models.Model):
    title = models.CharField(max_length=20, help_text='Enter your new task to accomplish!')
    description = models.TextField(max_length=200, blank=True, null=True, help_text='If you wanna be verbose about your task, here\'s your place, go ahead!')
    hashtag = models.ForeignKey(hashtag, on_delete=models.SET_NULL, blank=True, null=True, default='general')
    schedule_time_to_start = models.DateTimeField(blank=True, null=True, help_text='When do you plan to start with this task?')
    deadline = models.DateTimeField(blank=True, null=True, help_text='By when should you finish this task? (Let\'s all be real and put a realistic deadline!)')

    PRIORITY=(
        ('Q1', 'Do First'),
        ('Q2', 'Schedule'),
        ('Q3', 'Delegate'),
        ('Q4', 'Don\'t Do')
    )

    priority = models.CharField(max_length=2,choices=PRIORITY, blank=True, null=True, default='Q2',help_text='Choose a priority for your task.')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])

    class Meta:
        ordering = ['deadline', 'schedule_time_to_start']
