# Generated by Django 3.1.5 on 2021-01-12 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210111_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='studentsprojects',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projects'),
        ),
        migrations.AlterField(
            model_name='studentsprojects',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students'),
        ),
    ]
