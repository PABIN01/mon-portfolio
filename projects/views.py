from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    categories = Project.CATEGORY_CHOICES
    selected = request.GET.get('category', '')
    if selected:
        projects = projects.filter(category=selected)
    return render(request, 'projects/list.html', {
        'projects': projects,
        'categories': categories,
        'selected': selected,
        'active': 'projects',
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {
        'project': project,
        'active': 'projects',
    })
