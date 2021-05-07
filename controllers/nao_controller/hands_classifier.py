import pickle
import numpy as np

class HandsClassifier:
    def __init__(self, model_path):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, processed_frame: np.ndarray):
        return self.model.predict(processed_frame)[0]