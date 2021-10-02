# Generated by Django 3.1.5 on 2021-10-01 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210516_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.TextField(verbose_name='Марка машины')),
                ('model', models.TextField(verbose_name='Модель машины')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Имя студента')),
                ('surname', models.TextField(verbose_name='Фамилия студента')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
        migrations.CreateModel(
            name='DriversCars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cars')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.drivers')),
            ],
            options={
                'verbose_name': 'Проект студента',
                'verbose_name_plural': 'Проекты студентов',
            },
        ),
        migrations.CreateModel(
            name='DriversPhoto',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField(verbose_name='Ссылка на фото')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.drivers')),
            ],
            options={
                'verbose_name': 'Фото водителя',
                'verbose_name_plural': 'Фото водителей',
            },
        ),
        migrations.RemoveField(
            model_name='studentslessons',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='studentslessons',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentsphoto',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentsprojects',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='studentsprojects',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='teachersphotos',
            name='teacher',
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.AddField(
            model_name='clients',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание предмета'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='name',
            field=models.TextField(verbose_name='Имя клиента'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='surname',
            field=models.TextField(verbose_name='Фамилия клиента'),
        ),
        migrations.DeleteModel(
            name='EngineerProjects',
        ),
        migrations.DeleteModel(
            name='Lessons',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='StudentsLessons',
        ),
        migrations.DeleteModel(
            name='StudentsPhoto',
        ),
        migrations.DeleteModel(
            name='StudentsProjects',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
        migrations.DeleteModel(
            name='TeachersPhotos',
        ),
    ]
