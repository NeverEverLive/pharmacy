# Generated by Django 4.0 on 2021-12-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_drug_description_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.position'),
        ),
    ]
