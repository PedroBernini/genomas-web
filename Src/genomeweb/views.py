from django.shortcuts import render
from django.http import JsonResponse
from genomeweb.deeplearning import neuralNetworks
from genomeweb.deeplearning import operationsPermutation
from genomeweb.deeplearning import operationsWorld

def home(request):
    return render(request, 'home.html')
    

def gerar_nova_rede(request):
    if request.method == 'POST':
        deepQNetwork = neuralNetworks.DqnKeras(3)
        deepQNetwork.saveNetwork('genomeweb/redes/network.h5')
        return JsonResponse({'msg': 'Rede gerada com sucesso!'}, status=200)
