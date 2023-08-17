# Generated by Django 4.2.3 on 2023-08-08 19:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_ebooks_delete_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ebooks",
            name="_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]