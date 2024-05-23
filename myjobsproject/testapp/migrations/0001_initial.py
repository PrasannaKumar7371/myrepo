# Generated by Django 4.1 on 2024-04-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BngJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=30)),
                ("tittle", models.CharField(max_length=30)),
                ("eligibility", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=30)),
                ("phonenumber", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="HydJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=30)),
                ("tittle", models.CharField(max_length=30)),
                ("eligibility", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=30)),
                ("phonenumber", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="VizagJobs",
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
                ("date", models.DateField()),
                ("company", models.CharField(max_length=30)),
                ("tittle", models.CharField(max_length=30)),
                ("eligibility", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=30)),
                ("phonenumber", models.BigIntegerField()),
            ],
        ),
    ]