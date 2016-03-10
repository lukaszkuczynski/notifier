import pickle

class RawStateManager:

    def __init__(self, params):
        if params :
            self.filename = params['stateManager']['filename']

    def read(self):
        pass

    def save(self, state):
        f = open(self.filename, 'wb')
        pickle.dump(state, f)

