# Generated by Django 5.1.4 on 2025-04-04 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_article', models.AutoField(primary_key=True, serialize=False)),
                ('code_article', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=255)),
                ('categorie', models.CharField(blank=True, max_length=100, null=True)),
                ('unite', models.CharField(blank=True, max_length=50, null=True)),
                ('date_expiration', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=11)),
                ('quantite_unitaire', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthentificationArticle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'authentification_article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemandeAchat',
            fields=[
                ('id_demande', models.AutoField(primary_key=True, serialize=False)),
                ('quantite_demandee', models.IntegerField()),
                ('date_demande', models.DateField()),
                ('statut', models.CharField(blank=True, max_length=10, null=True)),
                ('remarques', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('prix_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'demande_achat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommandeAchat',
            fields=[
                ('id_commande', models.AutoField(primary_key=True, serialize=False)),
                ('date_commande', models.DateField()),
                ('statut', models.CharField(blank=True, max_length=10, null=True)),
                ('montant_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantite_demandee', models.IntegerField()),
                ('quantite_unitaire', models.IntegerField(default=0)),
                ('prix', models.IntegerField(blank=True, null=True)),
                ('prix_total', models.IntegerField(blank=True, null=True)),
                ('fournisseur', models.CharField(blank=True, max_length=255, null=True)),
                ('remarques', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'commande_achat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CommandeDemande',
            fields=[
                ('commande', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='commande_achat.commandeachat')),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='commande_achat.demandeachat')),
            ],
            options={
                'db_table': 'commande_demande',
                'managed': True,
                'unique_together': {('commande', 'demande')},
            },
        ),
    ]
