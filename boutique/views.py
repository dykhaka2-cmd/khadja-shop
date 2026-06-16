from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Categorie, Produit, Contact


def home(request):
    categories = Categorie.objects.all()
    produits_vedette = Produit.objects.filter(mis_en_avant=True, en_stock=True)[:6]
    return render(request, 'home.html', {
        'categories': categories,
        'produits_vedette': produits_vedette,
    })


def catalogue(request):
    categories = Categorie.objects.all()
    produits = Produit.objects.filter(en_stock=True)

    categorie_slug = request.GET.get('categorie')
    categorie_active = None
    if categorie_slug:
        categorie_active = get_object_or_404(Categorie, slug=categorie_slug)
        produits = produits.filter(categorie=categorie_active)

    return render(request, 'catalogue.html', {
        'categories': categories,
        'produits': produits,
        'categorie_active': categorie_active,
    })


def produit_detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    produits_similaires = Produit.objects.filter(
        categorie=produit.categorie, en_stock=True
    ).exclude(id=produit.id)[:4]
    return render(request, 'produit_detail.html', {
        'produit': produit,
        'produits_similaires': produits_similaires,
    })


def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        telephone = request.POST.get('telephone', '').strip()
        message_text = request.POST.get('message', '').strip()
        if nom and telephone and message_text:
            Contact.objects.create(nom=nom, telephone=telephone, message=message_text)
            messages.success(request, "✅ Message envoyé ! Nous vous contacterons très bientôt.")
            return redirect('contact')
        else:
            messages.error(request, "❌ Veuillez remplir tous les champs.")
    return render(request, 'contact.html')
