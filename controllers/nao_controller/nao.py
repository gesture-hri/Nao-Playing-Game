from controller import Robot
from nao_constants import NaoConstants
from move import Move

import warnings

class Nao(Robot):

    def __init__(self):
        super().__init__()
        self.time_step = int(self.getBasicTimeStep())
        self.current_move = None
        self.body = {
            part: {
                limb: {
                    axis: self.getDevice(part + limb + axis) 
                    for axis in NaoConstants.AXES if (limb, axis) not in NaoConstants.FORBIDDEN
                } if limb != NaoConstants.HAND else 
                    {i: self.getDevice(part + limb + str(i)) for i in range(1, NaoConstants.NUM_PHALANX + 1)}
                for limb in NaoConstants.LIMBS
            } for part in NaoConstants.PARTS
        }

    def _set_position(self, part, limb, axis, position):
        self.body[part][limb][axis].setPosition(position)

    def _set_velocity(self, part, limb, axis, velocity):
        self.body[part][limb][axis].setVelocity(velocity)

    def _set_move(self, move: Move):
        self.current_move = move
        move.start(self.getTime())

    def is_moving(self):
        return self.current_move and not self.current_move.is_completed(self.getTime())

    def play_motion(self, move: Move):
        self._set_move(move)
        for part, limbs in move.sequence.items():
            for limb, axes in limbs.items():
                for axis, (vel, pos) in axes.items():
                    self._set_velocity(part, limb, axis, vel)
                    self._set_position(part, limb, axis, pos)

    def step(self):
        return super().step(self.time_step)
