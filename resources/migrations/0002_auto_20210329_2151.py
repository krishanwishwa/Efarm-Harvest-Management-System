# Generated by Django 3.1.6 on 2021-03-29 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workers',
            old_name='waddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='workers',
            old_name='wcontact_number',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='workers',
            old_name='wemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='workers',
            old_name='wgender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='workers',
            old_name='wimage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='workers',
            old_name='wname',
            new_name='name',
        ),
    ]
