

---

# 🤝 SignConnect - Real-Time Indian Sign Language to Text & Speech Converter

**SignConnect** is a real-time deep learning application that bridges the gap between the Deaf and Hearing communities. Using gesture recognition, it translates **Indian Sign Language (ISL)** into **English text** and **speech**, enabling smoother and more inclusive communication.

---

## 🛠️ Tech Stack

* **Python** 🐍
* **OpenCV** 🎥 – Real-time video processing
* **MediaPipe** ✋ – Hand landmark detection
* **TensorFlow / Keras** 🧠 – CNN-based gesture classification
* **pyttsx3** 🔊 – Text-to-speech conversion
* **NumPy, PIL** 📊 – Image processing and data handling

---

## ✨ Features

* 🔤 Converts **Indian Sign Language gestures** to English text
* 🔊 Speaks the translated text using **text-to-speech**
* 🎥 Real-time gesture recognition from webcam feed
* 💡 User-friendly GUI for smooth interaction
* 🧠 Trained CNN model on a custom gesture dataset
* 🧪 Modular code structure for easy experimentation and extension

---

## 🔍 How It Works

1. **Hand Gesture Detection**: Uses **MediaPipe** to detect and track hand landmarks from the webcam.
2. **Preprocessing**: Captures and processes the hand region (cropped + resized).
3. **Gesture Prediction**: A trained **CNN model** predicts the class/label of the gesture.
4. **Output**: Displays the translated **text** and optionally converts it to **speech** using `gTTS`.

---

## 🗂️ Project Structure

```
SignConnect/
│
├── dataset/                 # Preprocessed gesture images for training
├── model/                   # Trained CNN model (model.h5)
├── HandTrackingModule.py    # MediaPipe hand detection module
├── main.py                  # Main application script with GUI
├── model_train.py           # Training script for CNN model
├── utils.py                 # Utility functions
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation
```

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Main Libraries:

* `opencv-python`
* `mediapipe`
* `tensorflow`
* `gtts`
* `tkinter` (built-in with Python on most systems)
* `numpy`
* `Pillow`

---

## 💡 Use Cases

* 🧏‍♂️ **Assistive Technology** for the Deaf community
* 🏫 **Educational Tool** for learning ISL and sign language recognition
* 🏥 **Healthcare Communication** with deaf/mute patients
* 📱 Future integration with **mobile apps** or **web platforms**
* 🧪 Research in Human-Computer Interaction (HCI) and accessibility

---

## 🚀 Future Improvements

* 🤖 **LSTM integration** for continuous sentence-level predictions
* 🌐 Deploy as a **web application** or **mobile app**
* 🌍 Support for **multiple sign languages** (e.g., ASL, BSL)
* 🧠 Improve accuracy with **larger datasets** and **Transfer Learning**
* 🎤 Add **speech-to-sign** mode for two-way interaction
* 🧩 Gesture correction and **auto-suggestion** for unclear signs

---


