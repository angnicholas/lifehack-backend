# Generated by Django 4.0.6 on 2022-07-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(default='tes', max_length=255),
            preserve_default=False,
        ),
    ]
