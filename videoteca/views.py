from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gioco
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Lista giochi come dizionari Python (collezioni!)
giochi = [
    {'titolo': 'Elder Realms', 'categoria': 'RPG'},
    {'titolo': 'Racing Thunder', 'categoria': 'FPS'},
    {'titolo': 'Indie Escape', 'categoria': 'INDIE'},
]

def home(request):
    #return HttpResponse("Benvenuti in Django Gaming!")
    return render(request, 'videoteca/home.html')

def lista_giochi(request):
# Passa la lista al template (come return di funzione)
    giochi = Gioco.objects.all() # SELECT * FROM videoteca_gioco
    return render(request, 'videoteca/lista.html', {'giochi': giochi})

def dettaglio_gioco(request, id):
# id dalla URL, come parametro funzione
    gioco = giochi[int(id)]
    return HttpResponse(
        f"<h1>{gioco['titolo']}</h1>"
        f"<p>Categoria: {gioco['categoria']}</p>"
    )
    
def catalogo(request):
    giochi_db = Gioco.objects.all() 
    return render(request, 'videoteca/catalogo.html', {
        'giochi': giochi_db,
        'totalegiochi': giochi_db.count()
    })

@login_required    
def aggiungigioco(request):
    if request.method == 'POST':
        Gioco.objects.create(
            titolo=request.POST['titolo'],
            categoria=request.POST['categoria'],
            anno=int(request.POST['anno']),
            recensione=request.POST.get('recensione', ''),
        )
        return redirect('catalogo') 
    return render(request, 'videoteca/aggiungi.html')

@login_required
def modificagioco(request, id):
    gioco = Gioco.objects.get(id=id)
    if request.method == 'POST':
        gioco.titolo = request.POST['titolo']
        gioco.categoria = request.POST['categoria']
        gioco.anno = int(request.POST['anno'])
        gioco.recensione = request.POST.get('recensione', '')
        gioco.save()
        return redirect('catalogo')
    return render(request, 'videoteca/modifica.html', {'gioco': gioco})

@login_required
def eliminagioco(request, id):
    Gioco.objects.get(id=id).delete()
    return redirect('lista')  