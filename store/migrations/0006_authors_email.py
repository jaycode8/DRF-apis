# Generated by Django 4.2.3 on 2023-08-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_authors"),
    ]

    operations = [
        migrations.AddField(
            model_name="authors",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
