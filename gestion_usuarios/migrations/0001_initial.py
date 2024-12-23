# Generated by Django 5.1.4 on 2024-12-11 19:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='path/to/upload')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(blank=True, max_length=50, null=True)),
                ('dni', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Carnet Identidad:')),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
