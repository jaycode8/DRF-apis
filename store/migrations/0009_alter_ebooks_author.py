# Generated by Django 4.2.3 on 2023-08-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_remove_test_id_test__id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ebooks", name="author", field=models.CharField(max_length=100),
        ),
    ]
