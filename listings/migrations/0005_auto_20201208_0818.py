# Generated by Django 3.1.2 on 2020-12-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201208_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
