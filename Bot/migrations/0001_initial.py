# Generated by Django 4.1.13 on 2024-07-05 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "db_table": "user_table",
                "unique_together": {("username", "email")},
            },
        ),
        migrations.CreateModel(
            name="Chat",
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
                ("message", models.CharField(max_length=500)),
                ("timestamp", models.DateTimeField()),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Bot.user",
                    ),
                ),
            ],
            options={
                "db_table": "message_table",
            },
        ),
    ]
