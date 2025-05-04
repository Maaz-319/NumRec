# 🧠 Digit Recognizer Android App

A simple Android app that recognizes handwritten digits using a Convolutional Neural Network (CNN) model integrated with TensorFlow Lite. Just draw a number (0–9), and the app will tell you what it thinks it is!

---

## 📱 Features
- ✍️ Draw digits using a custom `DrawingView`
- 🧠 Predict using a pre-trained TFLite CNN model (MNIST)
- 🎨 Clean dark-themed UI
- 🧹 Clear button to reset drawing
- 🔍 Preprocesses and normalizes bitmap before feeding into the model

---

## 🚀 Tech Stack

- **Kotlin** — for Android development
- **TensorFlow Lite** — for on-device ML inference
- **CNN model** — trained on MNIST dataset
- **Custom View** — to capture user handwriting

---

## 📦 How It Works

1. User draws a digit on screen.
2. Bitmap is resized to 28x28 and converted to grayscale.
3. Pixels are normalized to 0–1 range.
4. ByteBuffer is created and fed to the `.tflite` model.
5. Model returns an array of probabilities (0–9).
6. Highest value = predicted digit.

---

## 🧪 Main Learning Points

- Integrating `.tflite` model in Android app
- Preprocessing images in Kotlin
- Building custom drawing components
- ByteBuffer and normalization for ML input
- Understanding on-device ML inference

---

This project helped me understand how AI can be integrated in native Android apps.

---

## 🔗 Connect

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue)](https://www.linkedin.com/in/maazbinasif)
