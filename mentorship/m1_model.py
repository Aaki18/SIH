import pickle
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class MentorshipModel:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        try:
            with open('mentorship_model.pkl', 'rb') as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            self.model = KNeighborsClassifier()
            # You would typically train your model here

    def predict(self, skills, area_of_interest):
        # Example feature vector for prediction
        features = np.array([[skills, area_of_interest]])
        return self.model.predict(features)

    def train_model(self, X, y):
        self.model.fit(X, y)
        with open('mentorship_model.pkl', 'wb') as file:
            pickle.dump(self.model, file)
