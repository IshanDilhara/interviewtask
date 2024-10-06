
from django.db import models

class DynamicTable(models.Model):
    school_name = models.CharField(max_length=255)
    year = models.IntegerField()
    student_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_level = models.IntegerField()
    class_name = models.CharField(max_length=50)  # Renamed to avoid clash with reserved words
    subject = models.CharField(max_length=100)
    answers = models.TextField()
    correct_answers = models.TextField()
    question_number = models.IntegerField()
    subject_contents = models.TextField()
    assessment_areas = models.TextField()
    # Add the other fields similarly...
    # Ensure to have the correct names matching the CSV column names without spaces

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



