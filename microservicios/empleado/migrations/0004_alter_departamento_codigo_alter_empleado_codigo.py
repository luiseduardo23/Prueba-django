# Generated by Django 4.1.7 on 2023-03-16 04:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_alter_empleado_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='codigo',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='codigo',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
