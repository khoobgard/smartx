# Generated by Django 2.0 on 2020-05-18 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=300)),
                ('code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=300)),
                ('code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Master'),
        ),
    ]