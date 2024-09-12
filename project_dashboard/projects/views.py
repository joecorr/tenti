from django.shortcuts import render

def dashboard(request):
    # Simulate some fake data
    projects = [
        {'name': 'Project Alpha', 'description': 'This is project Alpha.', 'start_date': '2023-01-01'},
        {'name': 'Project Beta', 'description': 'This is project Beta.', 'start_date': '2023-02-01'},
        {'name': 'Project Gamma', 'description': 'This is project Gamma.', 'start_date': '2023-03-01'},
    ]
    
    # Pass the data to the template
    return render(request, 'dashboard.html', {'projects': projects})
