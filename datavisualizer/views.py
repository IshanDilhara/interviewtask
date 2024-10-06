import pandas as pd
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import DynamicTable

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        
        # Save the file to a temporary location if needed
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_path = fs.url(filename)

        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)

        # Rename columns to match the DynamicTable model field names
        df.rename(columns={
            'StudentID': 'student_id',
            'First Name': 'first_name',
            'Last Name': 'last_name',
            'Year Level': 'year_level',
            'Class': 'class_name',
            'Subject': 'subject',
            'Answers': 'answers',
            'Correct Answers': 'correct_answers',
            'Question Number': 'question_number',
            'Subject Contents': 'subject_contents',
            'Assessment Areas': 'assessment_areas',
            'sydney_correct_count_percentage': 'sydney_correct_count_percentage',
            'sydney_average_score': 'sydney_average_score',
            'sydney_participants': 'sydney_participants',
            'student_score': 'student_score',
            'student_total_assessed': 'student_total_assessed',
            'student_area_assessed_score': 'student_area_assessed_score',
            'total_area_assessed_score': 'total_area_assessed_score',
            'participant': 'participant',
            'correct_answer_percentage_per_class': 'correct_answer_percentage_per_class',
            'average_score': 'average_score',
            'school_percentile': 'school_percentile',
            'sydney_percentile': 'sydney_percentile',
            'strength_status': 'strength_status',
            'high_distinct_count': 'high_distinct_count',
            'distinct_count': 'distinct_count',
            'credit_count': 'credit_count',
            'participant_count': 'participant_count',
            'award': 'award'
        }, inplace=True)

        # Iterate over DataFrame rows and save to the DynamicTable model
        for index, row in df.iterrows():
            try:
                DynamicTable.objects.create(**row.to_dict())
            except Exception as e:
                print(f"Error saving row {index}: {e}")

        return redirect('visualize_data')  # Redirect to visualize data view

    return render(request, 'upload.html')

"""def visualize_data(request):
    # Logic to visualize data, for example, retrieving data from DynamicTable
    data = DynamicTable.objects.all()
    return render(request, 'visualize.html', {'data': data,})"""
    
from django.shortcuts import render
from .models import DynamicTable

def visualize_data(request):
    # Your logic to visualize data
    data = DynamicTable.objects.all()  # Example of querying the model
    return render(request, 'visualize.html', {'data': data})



def home(request):
    return render(request, 'home.html')


