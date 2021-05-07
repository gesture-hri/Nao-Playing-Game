from nao_constants import NaoConstants
from move import Move
class NaoMoves:
    STAND_STILL = Move(
        {
            NaoConstants.RIGHT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 1.5)
                },
                NaoConstants.WRIST: {
                    NaoConstants.YAW: (5.0, 0.0)
                },
                NaoConstants.HAND: {
                    i: (5.0, 0.0) for i in range(1, NaoConstants.NUM_PHALANX + 1)
                }
            },
            NaoConstants.LEFT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 1.5)
                },
                NaoConstants.WRIST: {
                    NaoConstants.YAW: (5.0, 0.0)
                },
                NaoConstants.HAND: {
                    i: (5.0, 0.0) for i in range(1, NaoConstants.NUM_PHALANX + 1)
                }
            }
        },
        NaoConstants.SHORT_TIME
    )

    RIGHT_HAND_ROCK = Move(
        {
            NaoConstants.RIGHT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 0.5)
                },
                NaoConstants.WRIST: {
                    NaoConstants.YAW: (5.0, 0.0)
                },
                NaoConstants.HAND: {
                    i: (5.0, 0.0) for i in range(1, NaoConstants.NUM_PHALANX + 1)
                }
            },
            NaoConstants.LEFT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 1.5)
                }
            }
        }, 
        NaoConstants.MEDIUM_TIME
    )

    RIGHT_HAND_PAPER = Move(
        {
            NaoConstants.RIGHT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 0.5)
                },
                NaoConstants.HAND: {
                    i: (5.0, 1.5) for i in range(1, NaoConstants.NUM_PHALANX + 1)
                }
            },
            NaoConstants.LEFT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 1.5)
                }
            }
        },
        NaoConstants.MEDIUM_TIME
    )

    RIGHT_HAND_SCISSORS = Move(
        {
            NaoConstants.RIGHT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 0.5)
                },
                NaoConstants.WRIST: {
                    NaoConstants.YAW: (5.0, 1.5)
                },
                NaoConstants.HAND: {
                    i: (5.0, 1.5) for i in range(1, 7)
                }
            },
            NaoConstants.LEFT: {
                NaoConstants.SHOULDER: {
                    NaoConstants.PITCH: (5.0, 1.5)
                }
            }
        }, 
        NaoConstants.MEDIUM_TIME
    )

