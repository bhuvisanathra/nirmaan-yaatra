# Generated by Django 5.0 on 2024-04-03 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("project_name", models.CharField(max_length=100)),
                ("start_date", models.DateTimeField(auto_now_add=True)),
                ("end_date", models.DateTimeField(auto_now=True)),
                ("budget", models.FloatField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("in_progress", "In Progress"),
                            ("completed", "Completed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("img_url", models.TextField(blank=True)),
                (
                    "location",
                    models.CharField(blank=True, default=None, max_length=100),
                ),
                ("city", models.CharField(blank=True, max_length=100)),
                (
                    "client_name",
                    models.CharField(blank=True, default=None, max_length=255),
                ),
                (
                    "client_number",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "client_address",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "client_city",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "client_email",
                    models.EmailField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
            ],
        ),
    ]
