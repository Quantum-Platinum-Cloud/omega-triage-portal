# Generated by Django 4.0 on 2022-01-01 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0020_attachment_case_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
