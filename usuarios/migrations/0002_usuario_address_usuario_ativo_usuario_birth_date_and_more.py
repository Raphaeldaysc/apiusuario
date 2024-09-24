# Generated by Django 5.1.1 on 2024-09-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='preferencia_notificacao',
            field=models.CharField(choices=[('E', 'E-mail'), ('S', 'SMS'), ('N', 'Nenhum')], default='E', max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
