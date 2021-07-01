# Generated by Django 3.2.3 on 2021-06-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(help_text='YYYY-MM-DD', verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('', '------'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], help_text='Not Required', max_length=6),
        ),
    ]