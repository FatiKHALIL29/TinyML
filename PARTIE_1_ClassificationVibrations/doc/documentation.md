📌 Documentation du Projet TinyML

🔍 Présentation

Ce projet a pour objectif de développer des systèmes d'intelligence embarquée (TinyML) pour deux applications principales :

Classification des Vibrations : Utilisation d'un modèle TinyML pour analyser les données de vibrations collectées via un capteur IMU (Inertial Measurement Unit) et classer ces vibrations en temps réel sur une plateforme embarquée.
Reconnaissance des Composants Électroniques : Utilisation d'une caméra pour capturer des images de composants électroniques, les classifier à l'aide d'un modèle pré-entraîné, puis envoyer les résultats vers un système d'automatisation comme Node-RED.
🔬 Partie 1 : Classification des Vibrations
📌 1. Acquisition des Données
Dans cette phase, un capteur IMU (Accéléromètre 3 axes) est utilisé pour collecter des données de vibrations. Ces données sont ensuite utilisées pour entraîner un modèle TinyML capable de classifier différents types de vibrations.

Code Arduino : data_generation.ino



📌 2. Entraînement du Modèle

Les données collectées sont utilisées pour entraîner un modèle d'apprentissage automatique qui sera ensuite déployé sur l'Arduino pour effectuer des classifications en temps réel.

Dataset : vibrations.csv

Le fichier contient les données d'accélération recueillies à partir de l'IMU, utilisées pour l'entraînement du modèle.

Notebook d'entraînement : training_vibrations.ipynb

Ce notebook contient tout le code nécessaire pour prétraiter les données, entraîner le modèle et évaluer ses performances.

Modèle obtenu : vibrations_model.tflite

Le modèle entraîné est ensuite converti en format TensorFlow Lite, prêt à être utilisé sur la plateforme Arduino.


📌 3. Inférence sur Arduino
Une fois le modèle entraîné et converti en format .tflite, il est déployé sur un Arduino Nano 33 BLE Sense pour effectuer une inférence en temps réel sur les vibrations.

Code Arduino : inference_vibrations.ino

Ce code charge le modèle sur l'Arduino et effectue l'inférence sur les données en temps réel. Les résultats sont affichés sur le moniteur série.


