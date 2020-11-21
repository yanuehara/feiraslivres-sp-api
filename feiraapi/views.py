from django.shortcuts import render
from rest_framework import generics
from .models import Feira
from .serializers import FeiraSerializer
from django.utils import timezone
import logging

logger = logging.getLogger("feiraapi.requests")

# Create your views here.

def logRequest(request):
    addr = request.META['REMOTE_ADDR']
    method = request.META['REQUEST_METHOD']
    path = request.path
    reqtime = timezone.localtime().isoformat()
    data = request.data
    ua = request.META['HTTP_USER_AGENT']
    log = f"[{reqtime}] {addr} --- {ua} --- {method} --- {path}"
    logger.info(log)
    if data:
        logger.info(data)

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
    
    def list(self, request, *args, **kwargs):
        logRequest(request)
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        logRequest(request)
        return super().create(request, *args, **kwargs)


class FeiraDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer

    def retrieve(self, request, *args, **kwargs):
        logRequest(request)
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        logRequest(request)
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        logRequest(request)
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        logRequest(request)
        return super().destroy(request, *args, **kwargs)