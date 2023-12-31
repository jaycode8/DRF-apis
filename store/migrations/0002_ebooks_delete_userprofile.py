# Generated by Django 4.2.3 on 2023-08-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="eBooks",
            fields=[
                ("username", models.CharField(max_length=100)),
                ("price", models.FloatField()),
                ("summary", models.TextField()),
                ("_id", models.UUIDField(primary_key=True, serialize=False)),
                ("website", models.URLField()),
                ("author", models.EmailField(max_length=254)),
                ("is_active", models.BooleanField(default=True)),
                ("created_timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(name="userProfile",),
    ]
