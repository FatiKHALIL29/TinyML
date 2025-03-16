## 📌 Objectif
Détecter et classifier différentes vibrations à l’aide de **l’IMU** de l’**Arduino Nano 33 BLE Sense**.

---

## 🚀 Étapes du projet
1. **Génération et collecte des données** (`data_generation.ino`)
   - Lire les données de l’IMU et les envoyer au PC via **Serial**.

2. **Entraînement du modèle** (`training_vibrations.ipynb`)
   - Entraîner un modèle de classification avec **TensorFlow Lite**.

3. **Inférence sur Arduino** (`inference_vibrations.ino`)
   - Charger le modèle `.tflite` et classifier les vibrations en temps réel.

---
