# Generated by Django 5.0.2 on 2024-07-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_otpcode_verified"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workouts",
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
                ("vedio", models.FileField(upload_to="workouts/")),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=1000)),
            ],
        ),
    ]