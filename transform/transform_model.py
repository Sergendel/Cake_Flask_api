import pickle
from sklearn.linear_model import LinearRegression


class TransformModel():
    def __init__(self, config):
        self.config = config
        self.__load_dependency()

    def __validation(self, dataset):
        pass

    def __load_dependency(self):

        with open(self.config.MODEL_PATH, 'rb') as f:
            self.model: LinearRegression = pickle.load(f)

    def predict(self, dataset):
        self.__validation(dataset)
        result= self.model.predict(dataset)
        return result
