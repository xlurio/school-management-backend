# Generated by Django 4.1.1 on 2022-09-16 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "register",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="registration number"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=256, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=256, verbose_name="last name"),
                ),
                (
                    "date_joined",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
        migrations.CreateModel(
            name="ClassRoom",
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
                ("subject", models.CharField(max_length=256, verbose_name="subject")),
                ("name", models.CharField(max_length=256, verbose_name="name")),
                ("start", models.DateField(verbose_name="start")),
                ("deadline", models.DateField(verbose_name="deadline")),
                (
                    "members",
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL, verbose_name="members"
                    ),
                ),
            ],
            options={
                "verbose_name": "class room",
                "verbose_name_plural": "class rooms",
            },
        ),
        migrations.CreateModel(
            name="Grade",
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
                ("grade", models.IntegerField(verbose_name="grade")),
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.classroom",
                        verbose_name="class room",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="student",
                    ),
                ),
            ],
            options={
                "verbose_name": "grade",
                "verbose_name_plural": "grades",
            },
        ),
        migrations.CreateModel(
            name="Absence",
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
                ("absence_date", models.DateField(verbose_name="date")),
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.classroom",
                        verbose_name="class room",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="student",
                    ),
                ),
            ],
            options={
                "verbose_name": "absence",
                "verbose_name_plural": "absences",
            },
        ),
    ]