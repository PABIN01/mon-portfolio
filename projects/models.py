from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('it', 'Projet IT'),
        ('entrepreneurial', 'Entrepreneurial'),
        ('startup', 'Accompagnement Startup'),
        ('freelance', 'Freelance'),
    ]
    

    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Catégorie")
    description = models.TextField(verbose_name="Description")
    technologies = models.CharField(max_length=500, verbose_name="Technologies utilisées", help_text="Séparées par des virgules")
    impact = models.TextField(verbose_name="Impact du projet", blank=True)
    features = RichTextField(verbose_name="Fonctionnalités principales de la plateforme", blank=True)
    objectives = models.TextField(verbose_name="Objectifs")
    results = models.TextField(verbose_name="Résultats")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Image")
    featured = models.BooleanField(default=False, verbose_name="Mis en avant")
    link = models.URLField(blank=True, null=True, verbose_name="Lien du projet")
    github = models.URLField(blank=True, null=True, verbose_name="Lien GitHub")
    created_at = models.DateField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',')]
    
    
    
    # autres champs...