from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('', views.algorithmsView, name='pagina_inicial'),
    path(r'dataset/', views.datasetView, name='dataset'),
    path(r'training/', views.trainingView, name='training'),

    #Create
    path(r'create_dataset/', views.createDataset, name='create_dataset'),
    path(r'create_network/', views.createNetwork, name='create_network'),

    #Delete
    path(r'delete_dataset/', views.deleteDataset, name='delete_dataset'),

    #Algorithms
    path(r'kececioglu_algorithm/', views.kececiogluAlgorithm, name='kececioglu_algorithm'),
    path(r'reinforcement_algorithm/', views.reinforcementAlgorithm, name='reinforcement_algorithm'),
]
