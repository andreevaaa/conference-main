# Generated by Django 4.0.5 on 2022-07-16 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0014_alter_author_faculty_alter_author_fio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scientificdirector',
            name='fio',
            field=models.CharField(help_text='Пример: Иванов Сергей Михайлович', max_length=150, verbose_name='ФИО полностью'),
        ),
    ]
