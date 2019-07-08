# Generated by Django 2.2.1 on 2019-07-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cargo', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[['T', 'Trainee'], ['M', 'Membro'], ['P', 'Pós Júnior']], max_length=1)),
            ],
        ),
    ]
