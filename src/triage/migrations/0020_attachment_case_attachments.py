# Generated by Django 4.0 on 2022-01-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0019_case_reported_dt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=1024)),
                ('content', models.BinaryField()),
                ('content_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='attachments',
            field=models.ManyToManyField(related_name='cases', to='triage.Attachment'),
        ),
    ]
