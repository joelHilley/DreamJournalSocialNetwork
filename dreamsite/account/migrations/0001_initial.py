from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('date_of_birth', models.DateField(help_text='YYYY-MM-DD', verbose_name='date of birth')),
                ('sex', models.CharField(choices=[('', '------'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], help_text='Not Required', max_length=6)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='date joined')),
                ('number_of_posts', models.PositiveSmallIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
