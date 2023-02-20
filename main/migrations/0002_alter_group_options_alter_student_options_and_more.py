# Generated by Django 4.1.7 on 2023-02-20 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterField(
            model_name='student',
            name='group_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.group', verbose_name='Группа'),
        ),
    ]