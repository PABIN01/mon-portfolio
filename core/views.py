# Views for the core app
from django.shortcuts import render
from projects.models import Project
from experience.models import Experience
from contact.models import ContactMessage
from contact.forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'featured_projects': featured_projects,
        'active': 'home',
    }
    return render(request, 'core/home.html', context)


def about(request):
    context = {
        'active': 'about',
        'skills': {
            'Réseaux': ['CCNA', 'Architecture réseau', 'Administration réseau', 'Protocoles TCP/IP'],
            'Cloud': ['AWS', 'Architecture cloud', 'Déploiement', 'DevOps'],
            'Cybersécurité': ['Sécurité réseau', 'Gestion des risques', 'Audit', 'CompTIA Security+'],
            'Management': ['Product Management', 'Leadership', 'Gestion de projet', 'Agile/Scrum'],
        }
    }
    return render(request, 'core/about.html', context)


def skills(request):
    context = {
        'active': 'skills',
    }
    return render(request, 'core/skills.html', context)
