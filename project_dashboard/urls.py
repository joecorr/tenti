from django.contrib import admin
from django.urls import path
from projection import views  # Make sure this is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route to home view
    path('dashboard/', views.dashboard, name='dashboard'),  # Route to the dashboard

]
