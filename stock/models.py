from django.db import models # type: ignore
from django.utils import timezone # type: ignore # Assurez-vous que Reception est bien défini
from article.models import Article
from reception.models import Reception
class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    code_article = models.CharField(max_length=50, unique=True)  # Code article unique
    designation = models.CharField(max_length=255)  # Nom de l'article
    unite = models.CharField(max_length=50, blank=True, null=True)  # Unité de mesure
    quantite_demandee = models.IntegerField(default=0)  # Quantité demandée
    stock_consomer = models.IntegerField(default=0)  # Stock consommé
    stock_total = models.IntegerField(default=0)  # Stock total
    unite = models.CharField(max_length=50, null=True, blank=True)
    id_reception = models.ForeignKey(
    Reception, on_delete=models.CASCADE, db_column="id_reception")
# Référence à la réception
    created_at = models.DateTimeField(default=timezone.now)  # Utilisation de default=timezone.now
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'stock'  # Force le nom de la table à 'stock'
    
    @property
    def quantite_restante(self):
        """Calcule la quantité restante automatiquement."""
        return max(self.stock_total - self.stock_consomer, 0)

    @property
    def alert(self):
        """Retourne True si le stock restant est inférieur ou égal à 2000."""
        return self.quantite_restante <= 2000

    def save(self, *args, **kwargs):
        """Vérification des valeurs avant sauvegarde."""
        if self.stock_total is None:
            self.stock_total = 0
        if self.stock_consomer < 0:
            raise ValueError("Le stock consommé ne peut pas être négatif.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.designation} ({self.code_article})"
    @property
    def quantite_restante(self):
        """Calcule la quantité restante, en gérant les valeurs nulles."""
        stock_total = self.stock_total or 0
        stock_consomer = self.stock_consomer or 0
        return stock_total - stock_consomer