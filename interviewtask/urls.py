from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('datavisualizer.urls')),  # Ensure the correct app name
    path('', RedirectView.as_view(url='/upload/')),  # Redirect root to upload page
]
