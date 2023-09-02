from django import forms
from .models import Attendance
from ..trainer.models import Trainer


class AttendanceAddForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['workout', 'login', 'logout', 'trained_by']
        widgets = {
            'workout': forms.Select(choices=[
                (None, '---'),
                ('Biceps', 'Biceps'),
                ('Triceps', 'Triceps'),
                ('Shoulders', 'Shoulders'),
                ('Chest', 'Chest'),
                ('ABS', 'ABS'),
                ('Back', 'Back'),
                ('Warm Up', 'Warm Up'),
                ('Treadmill', 'Treadmill'),
            ], attrs={'class': 'form-control mt-2', 'required': True}),
            'login': forms.DateTimeInput(
                attrs={'class': 'form-control mt-2', 'required': True, 'type': 'datetime-local'}),
            'logout': forms.DateTimeInput(
                attrs={'class': 'form-control mt-2', 'required': True, 'type': 'datetime-local'}),

            'trained_by': forms.Select(
                choices=[(None, "---")] + [(t.first_name, t.first_name) for t in Trainer.objects.all()],
                attrs={'class': 'form-control mt-2', 'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trained_by'].choices = [("None", '-')] + [(p.first_name, p.last_name) for p in
                                                               Trainer.objects.all()]
