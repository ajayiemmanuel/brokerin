# Generated by Django 5.0.3 on 2024-04-26 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0030_alert_kyc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='kyc',
            field=models.CharField(choices=[('swal-2', 'swal-2'), ('swal-4', 'swal-4')], default='#swal-4', max_length=24),
        ),
    ]
