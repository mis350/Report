# Generated by Django 3.2.4 on 2021-06-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_alter_report_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.IntegerField(choices=[(0, 'Kuwait City'), (1, 'Al Jahra'), (2, 'Hawalli'), (3, 'Farwaniyah'), (4, 'Mubarak Al-Kabeer'), (5, 'Al Ahmadi')]),
        ),
    ]