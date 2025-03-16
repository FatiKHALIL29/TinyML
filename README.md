
## **Résumé du Projet**

Ce projet TinyML est divisé en deux parties distinctes mais complémentaires, chacune visant à utiliser des techniques de machine learning embarqué (TinyML) pour des applications pratiques dans des environnements industriels et technologiques.

### **Partie 1 : Classification des Vibrations avec Arduino Nano 33 BLE et TensorFlow Lite**

Dans la première phase de ce projet, des données de vibrations sont générées en temps réel à l'aide du capteur IMU intégré à l'Arduino Nano 33 BLE. Ces données sont utilisées pour entraîner un modèle d'apprentissage automatique permettant de classifier différents types de vibrations. Une fois le modèle entraîné, il est déployé sur l'Arduino pour effectuer des classifications en temps réel. Cela permet de détecter des vibrations normales ou anormales, facilitant ainsi le diagnostic et la maintenance prédictive des systèmes.

### **Partie 2 : Classification des Composants avec Caméra et Node-RED**

La deuxième partie du projet se concentre sur la reconnaissance visuelle des composants électroniques. À l'aide d'une caméra, des images de composants électroniques sont capturées et traitées par un modèle d'apprentissage pré-entraîné. Les résultats de classification sont ensuite envoyés à Node-RED, un outil de développement pour l'Internet des objets (IoT), afin d'automatiser le traitement des données et d'intégrer le système dans un environnement de contrôle plus large.

## **Objectifs du Projet**

### **Partie 1 : Classification des Vibrations**
- Collecter et analyser des données de vibrations à l'aide du capteur IMU de l'Arduino Nano 33 BLE.
- Entraîner un modèle de machine learning avec TensorFlow Lite pour classifier les vibrations en fonction de leurs caractéristiques.
- Déployer le modèle sur la plateforme Arduino pour effectuer une classification des vibrations en temps réel et détecter des anomalies ou des conditions spécifiques.

### **Partie 2 : Classification des Composants**
- Capturer des images de composants électroniques à l'aide d'une caméra.
- Classifier ces images à l'aide d'un modèle pré-entraîné (par exemple, un modèle de classification d'images).
- Envoyer les résultats de la classification vers Node-RED pour effectuer des traitements supplémentaires, des actions automatisées ou des analyses en temps réel.

## **Technologies Utilisées**

- **Arduino Nano 33 BLE** : Plateforme embarquée utilisée pour la collecte de données de vibrations et le déploiement du modèle TinyML.
- **TensorFlow Lite** : Framework utilisé pour entraîner et déployer des modèles de machine learning optimisés pour les environnements embarqués.
- **Caméra** : Outil utilisé pour capturer des images des composants électroniques.
- **Node-RED** : Outil d'automatisation et de gestion des flux de données permettant d'intégrer la classification des composants dans un système de contrôle plus large.

