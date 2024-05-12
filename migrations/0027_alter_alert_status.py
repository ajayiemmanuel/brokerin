# Generated by Django 5.0.3 on 2024-04-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0026_alter_alert_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='status',
            field=models.CharField(choices=[('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.'), ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info')], default='sweetAlert', max_length=200, null=True),
        ),
    ]
