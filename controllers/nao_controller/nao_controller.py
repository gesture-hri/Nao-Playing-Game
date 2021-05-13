from nao import Nao
from nao_moves import NaoMoves
from camera_controller import CameraController
from frame_processor import FrameProcessor, Hands
from threading import Thread
from hands_classifier import HandsClassifier

import json
import pickle
import numpy as np
import sys
import os

config = json.load(open("cfg.json"))
sys.path.insert(0, os.path.abspath(config['preprocessor_class_path']))


RESPONSE_MAPPING = {
    0: NaoMoves.RIGHT_HAND_PAPER,
    1: NaoMoves.RIGHT_HAND_SCISSORS,
    2: NaoMoves.RIGHT_HAND_ROCK,
    None: NaoMoves.STAND_STILL
}


class NaoController:
    def __init__(self, classifier_path, preprocessor_path, response_mapping):
        self.response_mapping = response_mapping
        self.robot = Nao()
        self.camera_controller = CameraController()

        self.frame_preprocessor = pickle.load(open(preprocessor_path, 'rb'))
        self.classifier = pickle.load(open(classifier_path, 'rb'))
        
        self._flusher = Thread(target=self._flush, daemon=True)
        self._flusher.start()

    def _flush(self):
        while True:
            self.camera_controller.flush()

    def __del__(self):
        del self.camera_controller
       
    def step(self):
        return self.robot.step()

    def on_frame(self):
        frame = self.camera_controller.get_frame()
        if self.robot.is_moving():
            return
        processed = self.frame_preprocessor.preprocess(frame)
        label = self.classifier.predict(np.array([processed]))[0] if processed is not None else None
        self.robot.play_motion(self.response_mapping[label])


controller = NaoController(config["classifier_path"], config['preprocessor_file_path'], RESPONSE_MAPPING)

while controller.step() != -1:
    controller.on_frame()


