from django.shortcuts import render
from django.http import JsonResponse
from base.algorithms.deeplearning import neuralNetworks, operationsPermutation, operationsWorld, trainer
from base.algorithms import kececioglu
from base import models

from keras import backend as K

from os import listdir
from os.path import isfile, join

PATH_NETWORKS = 'base/algorithms/deeplearning/redes/'

def algorithmsView(request):
    datasets = models.DataSetPermutation.objects.all()
    networkArchives = [f for f in listdir(PATH_NETWORKS) if
                    isfile(join(PATH_NETWORKS, f))]
    context = {
        'datasets': datasets,
        'networkArchives': networkArchives
    }
    return render(request, 'algorithms.html', context)

def datasetView(request):
    datasets = models.DataSetPermutation.objects.all()
    context = {
        'datasets': datasets
    }
    return render(request, 'dataset.html', context)


def trainingView(request):
    return render(request, 'training.html')


def createDataset(request):
    tamanho = int(request.POST.get('tamanho'))
    quantidade = int(request.POST.get('quantidade'))
    minBkp = int(request.POST.get('minBkp'))
    maxBkp = int(request.POST.get('maxBkp'))
    nome = 'Dataset_' + str(tamanho) + '_' + str(quantidade) + '_' + str(minBkp) + '_' + str(maxBkp)

    try:
        permutations = operationsPermutation.generateDataSetPermutations(tamanho, quantidade, minBkp, maxBkp)
    except:
        return JsonResponse({'msg': 'Problemas em gerar estados!'}, status=400)

    textPermitations = str(permutations).replace('[[', '').replace(']]', '').replace(' ', '').replace('],[', ';')
    dataset = models.DataSetPermutation.objects.create(
        nome = nome,
        permutacoes = textPermitations,
        tamanho_permutacao = tamanho,
        quantidade = quantidade,
        minimo_breakpoints = minBkp,
        maximo_breakpoints = maxBkp
    )
    dataset.save()
    datasetInfo = {
        'id': dataset.id,
        'nome': nome,
        'tamanho': tamanho,
        'quantidade': quantidade,
        'minBkp': minBkp,
        'maxBkp': maxBkp
    }
    return JsonResponse({'msg': 'Dataset criado com sucesso!', 'dataset': datasetInfo}, status=200)


def createNetwork(request):
    tamanhoRede = int(request.POST.get('tamanhoRede'))
    epocas = int(request.POST.get('epocas'))
    lossFunction = request.POST.get('lossFunction')
    optimizer = request.POST.get('optimizer')
    nomeRede = 'Network_ ' + str(tamanhoRede) + '_' + str(epocas) + '_' + lossFunction + '_' + optimizer

    K.clear_session()
    try:
        dqn = trainer.createDqn(tamanhoRede, lossFunction=lossFunction, optimizerFunction=optimizer)
    except:
        return JsonResponse({'msg': 'Problemas ao criar a rede!'}, status=400)

    try:
        trainer.trainNetwork(dqn, epocas)
    except:
        return JsonResponse({'msg': 'Problemas durante o treinamento!'}, status=400)

    try:
        trainer.saveNetwork(dqn, nomeRede)
    except:
        return JsonResponse({'msg': 'Problemas durante o salvamento da rede!'}, status=400)

    return JsonResponse({'msg': 'Nova rede criada!'}, status=200)

def deleteDataset(request):
    idDataset = request.POST.get('idDataset')
    try:
        dataset = models.DataSetPermutation.objects.filter(pk=idDataset).first()
        dataset.delete()
        return JsonResponse({'msg': 'Dataset deletado com sucesso!'}, status=200)
    except:
        return JsonResponse({'msg': 'Problemas ao deletar dataset!'}, status=400)


def kececiogluAlgorithm(request):
    idDataset = request.POST.get('idDataset')

    try:
        dataset = models.DataSetPermutation.objects.filter(pk=idDataset).first()
        textPermutations = dataset.permutacoes
        permutations = [list(map(int, string.split(','))) for string in textPermutations.split(';')]

        aproximations = []
        for permutation in permutations:
            lowerBound = operationsPermutation.getLowerBound(permutation)
            realDistance = kececioglu.getDistanceToIdentity(permutation)
            if realDistance:
                aproximations.append(realDistance / lowerBound)

        mediaAproximation = sum(aproximations) / len(aproximations)
        return JsonResponse({'msg': 'Teste finalizado!  Aproximação do algoritmo Kececioglu: ' + str(mediaAproximation)},
                            status=200)
    except:
        return JsonResponse({'msg': 'Problemas durante o teste!'}, status=400)



def reinforcementAlgorithm(request):
    idDataset = request.POST.get('idDataset')
    modelo = request.POST.get('modelo')

    try:
        dataset = models.DataSetPermutation.objects.filter(pk=idDataset).first()
        textPermutations = dataset.permutacoes
        tamanhoPermutacao = dataset.tamanho_permutacao

        K.clear_session()
        dqn = neuralNetworks.DqnKeras(tamanhoPermutacao)
        try:
            dqn.loadNetwork(PATH_NETWORKS + modelo)
        except ValueError:
            return JsonResponse({'msg': 'O modelo possui tamanho da permutação diferente do Dataset!'}, status=400)
        permutations = [list(map(int, string.split(','))) for string in textPermutations.split(';')]

        competitions = []
        aproximations = []
        for permutation in permutations:
            lowerBound = operationsPermutation.getLowerBound(permutation)
            realDistance = operationsWorld.getDistanceToIdentity(permutation, dqn)
            if realDistance:
                if (realDistance / lowerBound) <= 2:
                    aproximations.append(realDistance / lowerBound)
                distanceKececioglu = kececioglu.getDistanceToIdentity(permutation)
                if realDistance == distanceKececioglu:
                    competitions.append(0)
                elif realDistance < distanceKececioglu:
                    competitions.append(1)
                else:
                    competitions.append(-1)

        kececiogluWin = competitions.count(-1) / len(competitions)
        draw = competitions.count(0) / len(competitions)
        rlWin = competitions.count(1) / len(competitions)

        if aproximations == []:
            return JsonResponse({'info': 'A rede não convergiu. Então ainda é incapaz de apontar as distâncias.'}, status=200)

        mediaAproximation = sum(aproximations) / len(aproximations)
        return JsonResponse({'msg': 'Teste finalizado! Aproximação do algoritmo de Reinforcement Learning: \n' + '\nMax: ' + str(max(aproximations)) + '\n' '\nMedia: ' + str(mediaAproximation) + '\n' '\nMin: ' + str(min(aproximations)) + '\n'}, status=200)
    except:
        return JsonResponse({'msg': 'Problemas durante o teste!'}, status=400)

def createDatasetTxt(request):
    idDataset = request.POST.get('idDataset')

    try:
        dataset = models.DataSetPermutation.objects.filter(pk=idDataset).first()
        textPermutations = dataset.permutacoes
        permutations = [list(map(int, string.split(','))) for string in textPermutations.split(';')]
        file = open("dataset6_100_13_10_14.txt", "w")
        for permutation in permutations:
            file.write(str(permutation) + '\n')
        file.close()
        return JsonResponse({'msg': 'Dataset Criado!'}, status=200)
    except:
        return JsonResponse({'msg': 'Problemas na criação do dataset!'}, status=400)
