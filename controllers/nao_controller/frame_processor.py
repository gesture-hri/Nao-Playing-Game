from itertools import chain
from hands_classifier import HandsClassifier
from enum import Enum

import mediapipe 
import numpy as np

class Hands(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    NONE = 3

class FrameProcessor:
    def __init__(self, classifier_path):
        self.classifier = HandsClassifier(classifier_path)
        self.processor = mediapipe.solutions.hands.Hands(
            static_image_mode=True,
            max_num_hands=1
        )

    def process_frame(self, frame: np.ndarray):
        processed = self.processor.process(frame)
        if not processed or not processed.multi_hand_landmarks:
            return Hands.NONE

        landmarks = np.array(list(chain.from_iterable([
            [landmark.x, landmark.y] 
            for landmark in processed.multi_hand_landmarks[0].landmark
        ])))
        
        return Hands(self.classifier.predict(np.array([landmarks])))
