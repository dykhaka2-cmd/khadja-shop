from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Produit(models.Model):
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name='produits'
    )
    nom = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='produits/')
    en_stock = models.BooleanField(default=True)
    mis_en_avant = models.BooleanField(default=False)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-date_envoi']

    def __str__(self):
        return f"{self.nom} — {self.telephone}"
