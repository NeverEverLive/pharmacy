# Generated by Django 4.0 on 2021-12-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_employee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]