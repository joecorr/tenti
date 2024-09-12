from django.contrib import admin
from django.urls import path
from projects import views  # Assuming your app is named `projects`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line for the dashboard
]
