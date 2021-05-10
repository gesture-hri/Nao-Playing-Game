from itertools import chain
from frame_processor import F
import cv2
import json
import mediapipe as mp
import numpy as np
import tensorflow_datasets as tsdf

mp_hands = mp.solutions.hands
config = json.load(open("cfg.json"))

def process_frame(frame: np.ndarray):
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1) as processor:
        result = processor.process(frame)
    return result


def postprocess_frame(processed):
    landmarks = [
        [landmark.x, landmark.y, landmark.z] 
        for landmark in processed.multi_hand_landmarks[0].landmark
    ]
    return np.array(list(chain.from_iterable(landmarks)))


paper = []
rock = []
scissors = []

failure_count = 0

dataset = tsdf.load('rock_paper_scissors')
for data in dataset['train']:
    label = data['label'].numpy()
    image = data['image'].numpy()

    processed = process_frame(image)
    if not processed.multi_hand_landmarks:
        failure_count += 1
        continue
    
    postprocessed = postprocess_frame(processed)
    if label == 0:
        rock.append(postprocessed)
    elif label == 1:
        paper.append(postprocessed)
    else:
        scissors.append(postprocessed)

paper = np.array(paper)
rock = np.array(rock)
scissors = np.array(scissors)

print("WARN: Failed to recognize hand on " + str(failure_count) + " samples")
print("INFO: data shapes - paper, rock, scissors: " + " ".join([str(paper.shape), str(rock.shape), str(scissors.shape)]))

np.save(config["paper_path"], paper)
np.save(config["rock_path"], rock)
np.save(config["scissors_path"], scissors)
