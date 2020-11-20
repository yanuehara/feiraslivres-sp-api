from django.shortcuts import render
from rest_framework import generics
from .models import Feira
from .serializers import FeiraSerializer

# Create your views here.

class FeirasList(generics.ListCreateAPIView):
    #queryset = Feira.objects.all()
    serializer_class = FeiraSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Feira.objects.all()
        distrito = self.request.query_params.get('distrito', None)
        if distrito is not None:
            distrito = distrito.upper()
            queryset = queryset.filter(distrito=distrito)
        
        regiao5 = self.request.query_params.get('regiao5', None)
        if regiao5 is not None:
            regiao5 = regiao5.capitalize()
            queryset = queryset.filter(regiao5=regiao5)
        
        nome_feira = self.request.query_params.get('nome_feira', None)
        if nome_feira is not None:
            nome_feira = nome_feira.upper()
            queryset = queryset.filter(nome_feira=nome_feira)
        
        bairro = self.request.query_params.get('bairro', None)
        if bairro is not None:
            bairro = bairro.upper()
            queryset = queryset.filter(bairro=bairro)

        return queryset

class FeiraDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer