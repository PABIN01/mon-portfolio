# Portfolio – Michael Benjamin Pabingui
> Site portfolio professionnel – Django 4.2 + Tailwind CSS

## 🚀 Installation rapide

```bash
# 1. Cloner / décompresser le projet
cd portfolio

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py migrate

# 5. Créer un superuser (pour l'admin)
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

Ouvrir : http://127.0.0.1:8000

## 🛠️ Structure du projet

```
portfolio/
├── portfolio/          # Config Django (settings, urls, wsgi)
├── core/               # Pages statiques (accueil, à propos, compétences)
├── projects/           # Modèle + vues projets
├── experience/         # Modèle + vues expériences (timeline)
├── contact/            # Formulaire de contact + modèle
├── templates/          # Tous les templates HTML
├── static/             # CSS, JS, images
└── requirements.txt
```

## 📋 Gestion du contenu

Tout le contenu (projets, expériences) se gère via l'admin Django :

**http://127.0.0.1:8000/admin/**

### Ajouter votre photo
Placez votre photo dans `static/images/michael.jpg`
Puis dans `templates/core/home.html`, décommentez la ligne :
```html
<img src="{% static 'images/michael.jpg' %}" alt="Michael Benjamin Pabingui">
```
Et supprimez la ligne `<div class="profile-placeholder">MBP</div>`

### Configurer l'email (envoi réel)
Dans `portfolio/settings.py`, remplacez :
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre@gmail.com'
EMAIL_HOST_PASSWORD = 'votre_mot_de_passe_app'
```

## 🌐 Déploiement (Render)

1. Créer un compte sur https://render.com
2. Nouveau Web Service → connecter votre repo GitHub
3. Build Command : `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
4. Start Command : `gunicorn portfolio.wsgi`
5. Variables d'environnement : `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`

## 📄 Pages disponibles

| URL | Description |
|-----|-------------|
| `/` | Accueil avec hero, rôles et projets mis en avant |
| `/about/` | Biographie, certifications, domaines d'expertise |
| `/experience/` | Timeline des expériences professionnelles |
| `/skills/` | Compétences avec barres animées |
| `/projects/` | Grille de projets avec filtre par catégorie |
| `/projects/<slug>/` | Détail d'un projet |
| `/contact/` | Formulaire de contact |
| `/admin/` | Interface d'administration |
