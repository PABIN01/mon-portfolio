import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_features_project_impact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="features",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, verbose_name="Fonctionnalités principales de la plateforme"
            ),
        ),
    ]