from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo,Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
def home(request):

   articoli=Articolo.objects.all()
   giornalisti=Giornalista.objects.all()
   context = {"articoli": articoli, "giornalisti": giornalisti}
   print(context)
   return render(request, "homepage_news.html", context)


def articoloDetailView(request, pk):
    articolo=get_object_or_404(Articolo,pk=pk)
    context={"articolo": articolo}
    return render(request, "articolo_detail.html", context)
# Create your views here.

class ArticoloDetailViewCB(DetailView):
    model = Articolo 
    template_name = "articolo_detail.html"


class ArticoloListView(ListView):
    model = Articolo
    template_name = "lista_articoli.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"]= Articolo.objects.all()
        return context 


class GiornalistaListView(ListView):
    model = Giornalista
    template_name = "lista_giornalisti.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giornalisti"]= Giornalista.objects.all()
        return context 

class GiornalistaDetailViewCB(DetailView):
    model = Giornalista 
    template_name = "giornalista_detail.html"