# Generated by Django 3.2.15 on 2022-08-27 18:19

import dblapp.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FactoryRecord",
            fields=[
                (
                    "factory_id",
                    models.CharField(
                        default=dblapp.models.random_string_1,
                        editable=False,
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("factory_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="OrgRecord",
            fields=[
                (
                    "org_id",
                    models.CharField(
                        default=dblapp.models.random_string_2,
                        editable=False,
                        max_length=4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("org_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="ItemRecord",
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
                (
                    "country",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("VN", "Vietnam"),
                            ("MY", "Malaysia"),
                            ("PH", "Philippines"),
                            ("SG", "Singapore"),
                            ("TH", "Thailand"),
                        ],
                        default="VN",
                        max_length=10,
                    ),
                ),
                ("execution_date", models.DateField(blank=True, null=True)),
                (
                    "fail_rate",
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(1.0),
                        ],
                    ),
                ),
                (
                    "defect_rate",
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(1.0),
                        ],
                    ),
                ),
                (
                    "factory_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dblapp.factoryrecord",
                    ),
                ),
                (
                    "org_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dblapp.orgrecord",
                    ),
                ),
            ],
        ),
    ]
