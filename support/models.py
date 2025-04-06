from django.db import models # type: ignore

class SupportMessage(models.Model):
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sujet
