
class NaoConstants:
    NUM_PHALANX = 8

    RIGHT = "R"
    LEFT = "L"
    SHOULDER = "Shoulder"
    ELBOW = "Elbow"
    WRIST = "Wrist"
    PITCH = "Pitch"
    ROLL = "Roll"
    YAW = "Yaw"
    HAND = "Phalanx"

    PARTS = [RIGHT, LEFT]

    LIMBS = [SHOULDER, ELBOW, WRIST, HAND]

    AXES = [YAW, PITCH, ROLL]

    FORBIDDEN = [(SHOULDER, YAW), (ELBOW, PITCH), (WRIST, PITCH), (WRIST, ROLL)]

    SHORT_TIME = 0.05
    MEDIUM_TIME = 0.5
    LONG_TIME = 1.0

    MOVE_SPEED = 5.0