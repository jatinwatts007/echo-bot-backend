# Generated by Django 4.1.13 on 2024-07-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Bot", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]