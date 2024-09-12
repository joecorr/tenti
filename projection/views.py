print("Loading projection/views.py")

from django.http import HttpResponse
from django.shortcuts import render

# Simulated project data
def dashboard(request):
    projects = [
        {"name": "Project Alpha", "status": "In Progress", "lead": "John Doe"},
        {"name": "Project Beta", "status": "Completed", "lead": "Jane Smith"},
        {"name": "Project Gamma", "status": "Not Started", "lead": "Alice Johnson"},
        {"name": "Project Delta", "status": "Completed", "lead": "Bob Adams"},
        {"name": "Project Epsilon", "status": "In Progress", "lead": "Charlie Brown"},
    ]

    total_projects = len(projects)
    recent_projects = projects[-3:]  # Get the 3 most recent projects

    return render(request, 'dashboard.html', {
        'total_projects': total_projects,
        'recent_projects': recent_projects
    })

def projects_list(request):
    projects = [
        {"name": "Project Alpha", "status": "In Progress", "lead": "John Doe"},
        {"name": "Project Beta", "status": "Completed", "lead": "Jane Smith"},
        {"name": "Project Gamma", "status": "Not Started", "lead": "Alice Johnson"},
        {"name": "Project Delta", "status": "Completed", "lead": "Bob Adams"},
        {"name": "Project Epsilon", "status": "In Progress", "lead": "Charlie Brown"},
    ]
    return render(request, 'projects.html', {'projects': projects})


def home(request):
    return HttpResponse("Hello World!")