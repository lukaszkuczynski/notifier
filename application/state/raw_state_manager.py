import pickle
import os

class RawStateManager:

    def __init__(self, params):
        if params :
            self.filename = params['stateManager']['filename']

    def read(self):
        if os.path.isfile(self.filename) :
            f = open(self.filename, 'rb')
            return pickle.load(f)
        else :
            return None

    def force_file(self, path):
        d = os.path.dirname(path)
        if len(d) > 0 :
            if not os.path.exists(d):
                os.makedirs(d)

    def save(self, state):
        self.force_file(self.filename)
        f = open(self.filename, 'wb+')
        pickle.dump(state, f)

