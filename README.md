Projet TinyML : Classification des Vibrations et des Composants

Ce projet est divisé en deux parties complémentaires, chacune visant à exploiter les capacités du machine learning sur des plateformes embarquées pour résoudre des problématiques spécifiques dans des domaines industriels.

1. Classification des Vibrations avec Arduino Nano 33 BLE et TensorFlow Lite
La première partie du projet consiste à collecter des données de vibrations à l'aide du capteur IMU de l'Arduino Nano 33 BLE. Ces données sont ensuite utilisées pour entraîner un modèle d'apprentissage automatique, qui permettra de classifier différents types de vibrations. Une fois le modèle entraîné, il est déployé directement sur l'Arduino, permettant ainsi de réaliser une classification en temps réel des vibrations et de détecter des anomalies ou des comportements spécifiques.

2. Classification des Composants avec Caméra et Node-RED
La deuxième partie du projet se concentre sur la reconnaissance visuelle de composants électroniques. À l'aide d'une caméra, des images de composants sont capturées et classifiées à l'aide d'un modèle d'apprentissage pré-entraîné. Les données de classification sont ensuite envoyées à Node-RED pour un traitement et une automatisation plus poussés, facilitant ainsi le contrôle et l'intégration dans des systèmes plus complexes.

Objectifs
Partie 1 : Générer des données de vibrations, entraîner un modèle avec TensorFlow Lite, et déployer ce modèle sur l'Arduino pour effectuer une classification des vibrations en temps réel.
Partie 2 : Utiliser une caméra pour capturer des images de composants électroniques, classifier ces images à l'aide d'un modèle pré-entraîné, puis envoyer les résultats vers Node-RED pour l'automatisation et le contrôle des processus.
