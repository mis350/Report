# Generated by Django 3.2.4 on 2021-06-24 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_alter_reportstatus_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportstatus',
            name='Report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.report'),
        ),
    ]
