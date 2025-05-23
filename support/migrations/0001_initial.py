# Generated by Django 5.2 on 2025-04-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupportMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_envoye', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
