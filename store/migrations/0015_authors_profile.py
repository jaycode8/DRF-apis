# Generated by Django 4.2.3 on 2023-08-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0014_test2_test3"),
    ]

    operations = [
        migrations.AddField(
            model_name="authors",
            name="profile",
            field=models.ImageField(default=1, upload_to="images/"),
            preserve_default=False,
        ),
    ]
