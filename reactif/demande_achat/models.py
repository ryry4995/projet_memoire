# This is an auto-generated Django model module.
from django.db import models


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    code_article = models.CharField(max_length=50)
    designation = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100, blank=True, null=True)
    unite = models.CharField(max_length=50, blank=True, null=True)
    date_expiration = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=11)
    quantite_unitaire = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthentificationArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authentification_article'


class DemandeAchat(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('approuve', 'Approuvé'),
        ('refuse', 'Refusé'),
    ]
    id_demande = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    quantite_demandee = models.IntegerField()
    date_demande = models.DateField(verbose_name="Date de la demande") 
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente') # type: ignore
    remarques = models.CharField(max_length=255, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Saisir manuellement ou calculer
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)  # Défini automatiquement
    updated_at = models.DateTimeField(auto_now=True)  # Mis à jour automatiquement

    class Meta:
        managed = True
        db_table = 'demande_achat'

    def save(self, *args, **kwargs):
        # Calcul automatique du prix total
        if self.prix and self.quantite_demandee:  # Vérifier que les deux valeurs sont définies
            self.prix_total = self.quantite_demandee * self.prix
        super().save(*args, **kwargs)
        
    def create_commande(self):
        # Import CommandeAchat et CommandeDemande à l'intérieur de la méthode pour éviter les imports circulaires
        from commande_achat.models import CommandeAchat, CommandeDemande
        import datetime
        
        # Vérifier si la demande est approuvée
        if self.statut != 'approuve':
            return None
            
        # Vérifier si la demande est déjà associée à une commande
        try:
            commande_demande = CommandeDemande.objects.get(demande=self)
            # Si une commande existe déjà, on retourne cette commande
            return commande_demande.commande
        except CommandeDemande.DoesNotExist:
            # Créer une nouvelle commande d'achat
            commande = CommandeAchat.objects.create(
                date_commande=datetime.date.today(),
                statut='en_cours',
                montant_total=self.prix_total,
                fournisseur='À déterminer',  # À mettre à jour plus tard
                remarques=f"Commande créée à partir de la demande #{self.id_demande}"
            )
            
            # Créer l'association entre la commande et la demande
            CommandeDemande.objects.create(commande=commande, demande=self)
            
            return commande


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
