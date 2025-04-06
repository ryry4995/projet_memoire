from django.db import models  # type: ignore
from commande_achat.models import CommandeAchat
from article.models import Article

class Reception(models.Model):
    id_reception = models.AutoField(primary_key=True)
    id_commande = models.ForeignKey(CommandeAchat, on_delete=models.CASCADE, db_column="id_commande")
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, db_column="id_article")
    code_article = models.CharField(max_length=50)
    quantite_unitaire = models.IntegerField(default=0)
    designation = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100, null=True, blank=True)
    unite = models.CharField(max_length=50, null=True, blank=True)
    date_expiration = models.DateField(null=True, blank=True)
    date_reception = models.DateField(null=True, blank=True)
    quantite_demandee = models.IntegerField()
    quantite_receptionnee = models.IntegerField(null=True, blank=True)
    STATUT_CHOICES = [
        ('Non réceptionné', 'Non réceptionné'),
        ('Réceptionné', 'Réceptionné'),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='Non réceptionné')

    

    class Meta:
        db_table = "reception"  # Assure que Django pointe vers la bonne table dans MySQL

    def __str__(self):
        return f"Réception {self.id_reception} - {self.designation}"
