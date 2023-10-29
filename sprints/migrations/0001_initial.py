# Generated by Django 4.2.6 on 2023-10-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0008_delete_sprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('tasks', models.ManyToManyField(blank=True, related_name='sprints', to='tasks.task')),
            ],
        ),
    ]
