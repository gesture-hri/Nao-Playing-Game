from nao import Nao
from nao_moves import NaoMoves
from camera_controller import CameraController
from frame_processor import FrameProcessor, Hands
from threading import Thread

import json

config = json.load(open("cfg.json"))

RESPONSE_MAPPING = {
    Hands.ROCK: NaoMoves.RIGHT_HAND_PAPER,
    Hands.PAPER: NaoMoves.RIGHT_HAND_SCISSORS,
    Hands.SCISSORS: NaoMoves.RIGHT_HAND_ROCK,
    Hands.NONE: NaoMoves.STAND_STILL
}


class NaoController:
    def __init__(self, classifier_path, response_mapping):
        self.response_mapping = response_mapping
        self.robot = Nao()
        self.camera_controller = CameraController()
        self.frame_processor = FrameProcessor(classifier_path)
        
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
        label = self.frame_processor.process_frame(frame)
        self.robot.play_motion(self.response_mapping[label])


controller = NaoController(config["sgd_classifier_path"], RESPONSE_MAPPING)

while controller.step() != -1:
    controller.on_frame()


