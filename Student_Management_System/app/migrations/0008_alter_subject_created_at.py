# Generated by Django 3.2 on 2023-09-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_subject_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
