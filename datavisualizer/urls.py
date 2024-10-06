from django.urls import path
from .views import upload_file, visualize_data, home

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('visualize/', visualize_data, name='visualize_data'),  # Ensure the path is correct
    path('', home, name='home'),
]


from django.urls import path
from .views import visualize_data

