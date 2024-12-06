# Generated by Django 5.1.4 on 2024-12-06 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='celestial/%Y/%m/%d')),
                ('celestial_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='main.celestial')),
            ],
        ),
    ]
