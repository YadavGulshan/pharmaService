# Generated by Django 4.0.1 on 2022-01-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_alter_medical_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='medical',
            name='website',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]