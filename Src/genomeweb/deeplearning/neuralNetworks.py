# Este arquivo contem todas as Redes Neurais

import keras
from keras.models import Sequential
from keras.layers import Dense

# DEVO PENALIZAR
# DEVO PENALIZAR NO MOMENTO QUE ELE AUMENTAR O BKP
# DEVO MELHORAR TEMPERATURA (COMECA BAIXO, TERMINA ALTO)
class DqnKeras(object):
    def __init__(self, permutation_size, gamma = 0.99, temperature = 0.5):
        self.permutation_size = permutation_size
        self.gamma = gamma
        self.temperature = temperature
        self.movesLimit = permutation_size * 2
        self.bkpReversals = False
        self.model = Sequential()
        self.model.add(Dense(150, activation='relu', input_shape=(permutation_size * 2,)))
        self.model.add(Dense(1, activation='tanh'))
        self.model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['accuracy']) # VERIFICAR ERROS!

    def saveNetwork(self, filepath):
        self.model.save_weights(filepath)
            
    def loadNetwork(self, filepath):
        self.model.load_weights(filepath)