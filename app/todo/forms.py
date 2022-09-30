from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from todo.models import StatusChoices

class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Name of task',
                                widget=forms.TextInput({'class': 'form-input'}))
    detail_description = forms.CharField(max_length=2000, required=True, label='Description',
                                       widget=widgets.Textarea)
    status = forms.ChoiceField(choices=StatusChoices.choices, label='Status')
    lead_at = forms.DateField(required=False, widget=widgets.SelectDateWidget, label='Lead_at')

    def clean_task_text(self):
        task_text = self.cleaned_data.get('task_text')
        if len(task_text) < 2:
            raise ValidationError('Not one symbol')
        return task_text