# Models for the experience app
from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name="Poste")
    company = models.CharField(max_length=200, verbose_name="Entreprise")
    location = models.CharField(max_length=100, blank=True, verbose_name="Lieu")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    is_current = models.BooleanField(default=False, verbose_name="Poste actuel")
    description = models.TextField(verbose_name="Description")
    missions = models.TextField(verbose_name="Missions principales", help_text="Une mission par ligne")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.title} – {self.company}"

    def get_missions_list(self):
        return [m.strip() for m in self.missions.splitlines() if m.strip()]

    def get_period(self):
        start = self.start_date.strftime('%Y')
        if self.is_current:
            return f"{start} – Présent"
        elif self.end_date:
            return f"{start} – {self.end_date.strftime('%Y')}"
        return start
