import cv2
import numpy as np
import math
import pyttsx3  # For text-to-speech
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Initialize camera and models
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Constants
offset = 20
imgSize = 300
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Word formation variables
detected_letters = []
current_word = ""
pending_letter = None
speak_enabled = False


def speak_word():
    """Function to convert current word to speech"""
    if current_word:
        engine.say(current_word)
        engine.runAndWait()


def draw_button(img, text, position, size, color):
    """Helper function to draw clickable buttons"""
    x, y = position
    w, h = size
    cv2.rectangle(img, (x, y), (x + w, y + h), color, cv2.FILLED)
    cv2.putText(img, text, (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return x, y, w, h


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the image
    imgOutput = img.copy()
    hands, img = detector.findHands(img, flipType=False)  # Already flipped

    # Create blank white image for processing
    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
    imgCrop = None

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        aspectRatio = h / w

        try:
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) // 2)
                imgWhite[:, wGap:wGap + wCal] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) // 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            pending_letter = labels[index]

            cv2.rectangle(imgOutput, (x, y - 50), (x + 90, y), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, pending_letter, (x + 20, y - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset),
                          (x + w + offset, y + h + offset), (255, 0, 255), 2)

        except Exception as e:
            pass

    # Draw word display background
    cv2.rectangle(imgOutput, (0, 0), (img.shape[1], 70), (50, 50, 50), cv2.FILLED)
    cv2.putText(imgOutput, f"Current Word: {current_word}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

    # Draw control buttons
    button_speak = draw_button(imgOutput, "SPEAK", (img.shape[1] - 150, img.shape[0] - 50), (140, 40), (50, 150, 50))
    button_clear = draw_button(imgOutput, "CLEAR", (img.shape[1] - 300, img.shape[0] - 50), (140, 40), (50, 50, 150))

    # Show processing windows
    if imgCrop is not None and imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
        cv2.imshow("Hand Sign", imgCrop)

    cv2.imshow("Processed Image", imgWhite)
    cv2.imshow("Sign Language to Text", imgOutput)


    # Handle mouse clicks for buttons
    def mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Check if speak button was clicked
            bx, by, bw, bh = button_speak
            if bx <= x <= bx + bw and by <= y <= by + bh:
                speak_word()

            # Check if clear button was clicked
            bx, by, bw, bh = button_clear
            if bx <= x <= bx + bw and by <= y <= by + bh:
                global current_word, detected_letters
                detected_letters = []
                current_word = ""


    cv2.setMouseCallback("Sign Language to Text", mouse_click)

    # Keyboard controls
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s') and pending_letter is not None:
        detected_letters.append(pending_letter)
        current_word = ''.join(detected_letters)
    elif key == ord(' '):  # Space bar also triggers speech
        speak_word()

cap.release()
cv2.destroyAllWindows()
