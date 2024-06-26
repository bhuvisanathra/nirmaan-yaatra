# Generated by Django 5.0 on 2024-04-03 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                ("amount", models.FloatField()),
                ("date", models.DateField(auto_now_add=True)),
                ("description", models.TextField()),
                ("is_approved", models.BooleanField(blank=True, default=False)),
                ("category", models.CharField(blank=True, max_length=30)),
                (
                    "status",
                    models.CharField(blank=True, default="pending", max_length=20),
                ),
                ("dealer_name", models.CharField(blank=True, max_length=100)),
                ("dealer_phone", models.CharField(blank=True, max_length=20)),
                (
                    "projects",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]
