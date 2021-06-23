# Generated by Django 3.0.2 on 2021-06-22 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResCivilId', models.IntegerField()),
                ('ResName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('civilid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Roads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoadNo', models.CharField(max_length=50)),
                ('RoadName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Road_name', models.TextField()),
                ('Accident_type', models.IntegerField(choices=[(0, 'New Report'), (1, 'In Progress'), (2, 'Done')], default=0)),
                ('location', models.IntegerField(choices=[(0, 'Kuwait City'), (1, 'Al Jahra'), (2, 'Hawalli'), (3, 'Farwaniyah'), (4, 'Mubarak Al-Kabeer'), (5, 'Al Ahmadi')])),
                ('Accident_Address', models.TextField(blank=True, null=True)),
                ('Accident_Describtion', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Two car crash'), (1, 'Multi car crash'), (2, 'Car crash with Injury'), (3, 'Car crash with Death'), (4, 'Car crash with Fire')])),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Receiver')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Reporter')),
            ],
        ),
    ]
