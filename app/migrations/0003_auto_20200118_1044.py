# Generated by Django 2.1.5 on 2020-01-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200118_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Category'),
        ),
    ]
