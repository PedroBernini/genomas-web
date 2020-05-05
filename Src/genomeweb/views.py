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

dicionario = {
    '[1, 2, 3, 2, 1, 3]' : 'arrow right',
    '[1, 2, 3, 3, 2, 1]' : 'arrow down-right',
    '[1, 2, 3, 1, 3, 2]' : 'arrow down',
    '[1, 3, 2, 3, 1, 2]' : 'arrow right',
    '[1, 3, 2, 2, 3, 1]' : 'arrow up-right',
    '[1, 3, 2, 1, 2, 3]' : 'arrow up',
    '[2, 1, 3, 1, 2, 3]' : 'arrow left',
    '[2, 1, 3, 3, 1, 2]' : 'arrow down',
    '[2, 1, 3, 2, 3, 1]' : 'arrow right',
    '[2, 3, 1, 3, 2, 1]' : 'arrow down',
    '[2, 3, 1, 1, 3, 2]' : 'arrow down-left',
    '[2, 3, 1, 2, 1, 3]' : 'arrow left',
    '[3, 1, 2, 1, 3, 2]' : 'arrow left',
    '[3, 1, 2, 2, 1, 3]' : 'arrow up',
    '[3, 1, 2, 3, 2, 1]' : 'arrow right',
    '[3, 2, 1, 2, 3, 1]' : 'arrow up',
    '[3, 2, 1, 1, 2, 3]' : 'arrow up-left',
    '[3, 2, 1, 3, 1, 2]' : 'arrow left'
}


def atualizar_politicas(request):
    if request.method == 'POST':
        deepQNetwork = neuralNetworks.DqnKeras(3)
        deepQNetwork.loadNetwork('genomeweb/redes/network.h5')
        scores = operationsPermutation.getAllScores(deepQNetwork.model)
        politicas = {}
        for score in scores:
            permutation = score[0][0]

            result = score[0][2]
            position = 0
            
            if score[1][2] > result:
                result = score[1][2]
                position = 1

            if score[2][2] > result:
                result = score[2][2]
                position = 2
            
            politicas[str(permutation)] = dicionario[str(score[position][0] + score[position][1])]

        return JsonResponse({'msg': 'Políticas atualizada com sucesso!', 'politicas': politicas}, status=200)


def treinar_rede(request):
    if request.method == 'POST':
        epochs = int(request.POST.get('epochs'))
        deepQNetwork = neuralNetworks.DqnKeras(3)
        deepQNetwork.loadNetwork('genomeweb/redes/network.h5')
        operationsWorld.worldTrain(deepQNetwork, epochs)
        deepQNetwork.saveNetwork('genomeweb/redes/network.h5')
        return JsonResponse({'msg': 'Rede treinada com sucesso!'}, status=200)