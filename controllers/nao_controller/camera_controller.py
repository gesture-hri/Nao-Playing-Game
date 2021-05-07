import mediapipe as mp
import cv2 

class CameraController:
    def __init__(self):
        self.camera_connection = cv2.VideoCapture(0)

        if not self.camera_connection.isOpened():
            raise Exception("Failed to connect to camera")

    def __del__(self):
        self.camera_connection.release()

    def flush(self):
        self.camera_connection.grab()

    def get_frame(self):
        return self.camera_connection.read()[1]
