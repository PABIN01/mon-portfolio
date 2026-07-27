# Views for the experience app
from django.shortcuts import render
from .models import Experience

def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'experience/list.html', {'experiences': experiences, 'active': 'experience'})
