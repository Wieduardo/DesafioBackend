# Generated by Django 4.1.3 on 2022-11-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CNABdoc",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.PositiveIntegerField()),
                ("date", models.DateField()),
                ("value", models.FloatField()),
                ("cpf", models.PositiveBigIntegerField()),
                ("card", models.CharField(max_length=50)),
                ("hour", models.TimeField()),
                ("owner", models.CharField(max_length=50)),
                ("store", models.CharField(max_length=50)),
                ("cnab_doc", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="CNABfile",
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
                ("cnab_doc", models.FileField(unique=True, upload_to="")),
            ],
        ),
    ]