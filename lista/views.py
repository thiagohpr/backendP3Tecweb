from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Lista
from .serializers import ListaSerializer

@api_view(['GET','POST','DELETE'])
def api_lista(request,lista_id):
    try:
        lista = Lista.objects.get(id=lista_id)
    except Lista.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_lista_data = request.data
        lista.title = new_lista_data['title']
        lista.score = new_lista_data['score']
        lista.state = new_lista_data['state']
        lista.url = new_lista_data['url']
        lista.save()

    if request.method == 'DELETE':
        lista.delete()
        
    serialized_lista = ListaSerializer(lista)
    return Response(serialized_lista.data)


@api_view(['GET','POST'])
def api_all(request):
    all_listas=Lista.objects.all()

    if request.method == 'POST':
        new_lista_data = request.data
        lista=Lista()
        lista.title=new_lista_data['title']
        lista.score = new_lista_data['score']
        lista.state = new_lista_data['state']
        lista.url = new_lista_data['url']
        lista.save()

        all_listas=Lista.objects.all()
    serialized_lista = ListaSerializer(all_listas,many=True)
    return Response(serialized_lista.data)