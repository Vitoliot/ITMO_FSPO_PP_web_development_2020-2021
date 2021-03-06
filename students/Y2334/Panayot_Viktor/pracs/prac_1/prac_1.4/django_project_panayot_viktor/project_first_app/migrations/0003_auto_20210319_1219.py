# Generated by Django 3.1.7 on 2021-03-19 09:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('project_first_app', '0002_examplemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
        migrations.AlterModelOptions(
            name='CarOwner',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='CarOwner',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='Adress_of_Home',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='Citizenship',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='Passport_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='password',
            field=models.CharField(default=1234, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='CarOwner',
            name='username',
            field=models.CharField(default='user', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='CarOwner',
            name='Date_of_Birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='CarOwner',
            name='Name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='CarOwner',
            name='Surname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
