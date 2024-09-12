print("Loading projection/views.py")

from django.http import HttpResponse
from django.shortcuts import render

# Simulated project data
def dashboard(request):
    projects = [
        {"name": "Project Alpha", "status": "In Progress", "lead": "John Doe"},
        {"name": "Project Beta", "status": "Completed", "lead": "Jane Smith"},
        {"name": "Project Gamma", "status": "Not Started", "lead": "Alice Johnson"},
    ]
    return render(request, 'dashboard.html', {'projects': projects})

def home(request):
    return HttpResponse("Hello World!")