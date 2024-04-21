# Generated by Django 4.0.3 on 2022-06-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_category_project_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('MINI_PROJECT', 'MINI_PROJECT'), ('FINAL_PROJECT', 'FINAL_PROJECT')], max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.CharField(max_length=100),
        ),
    ]
