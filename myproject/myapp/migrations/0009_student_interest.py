# Generated by Django 4.2 on 2025-05-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_student_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='interest',
            field=models.TextField(blank=True, null=True),
        ),
    ]
