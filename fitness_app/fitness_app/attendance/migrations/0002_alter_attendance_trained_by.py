# Generated by Django 4.2.4 on 2023-09-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='trained_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
