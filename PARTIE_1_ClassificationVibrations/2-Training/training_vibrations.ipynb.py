import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 🔹 Charger les données CSV
data = pd.read_csv("data1.csv")
print("📊 Aperçu des premières lignes :\n", data.head())

# 🔹 Encoder les labels (transformation texte -> nombre)
encoder = LabelEncoder()
data["label"] = encoder.fit_transform(data["label"])

# 🔹 Vérifier l'encodage
print("\n📌 Données après encodage :\n", data.head())
print("🎯 Classes encodées :", dict(enumerate(encoder.classes_)))

# 🔹 Visualisation de la répartition des classes
plt.figure(figsize=(6,4))
data["label"].value_counts().plot(kind='bar', color=["skyblue", "orange"])
plt.xlabel("Classes de vibration")
plt.ylabel("Nombre d'échantillons")
plt.title("Distribution des Classes")
plt.show()

# 🔹 Séparer les features (x, y, z) et les labels
X = data[['x', 'y', 'z']].values  
y = data['label'].values  

# 🔹 Normalisation des données (meilleur apprentissage)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 🔹 Séparation en entraînement (80%) et test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n📌 Taille des données d'entraînement :", X_train.shape)
print("📌 Taille des données de test :", X_test.shape)

# 🔹 Définition du modèle de classification
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),  # 3 entrées : x, y, z
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),  # Augmenté pour éviter l'overfitting
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Classification binaire
])

# 🔹 Compilation du modèle avec EarlyStopping
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 🔹 Early Stopping pour éviter un sur-entraînement
early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True)

# 🔹 Entraînement
history = model.fit(X_train, y_train, epochs=100, batch_size=8,
                    validation_data=(X_test, y_test), callbacks=[early_stopping])

# 🔹 Visualisation de l'apprentissage
plt.figure(figsize=(8,4))
plt.plot(history.history['loss'], label="Perte entraînement", color="blue")
plt.plot(history.history['val_loss'], label="Perte validation", color="red")
plt.xlabel("Épochs")
plt.ylabel("Perte")
plt.legend()
plt.title("Courbe de Perte du Modèle")
plt.show()

# 🔹 Convertir le modèle en TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 🔹 Sauvegarder le modèle TFLite
with open("vibrations_model.tflite", "wb") as f:
    f.write(tflite_model)

print("\n✅ Modèle TFLite sauvegardé sous vibrations_model.tflite")

# 🔹 Télécharger le modèle sur Google Colab (si nécessaire)
try:
    from google.colab import files
    files.download("vibrations_model.tflite")
except:
    print("📌 Téléchargement ignoré (exécution locale)")

# 🔹 Charger le modèle TFLite en bytes
with open("vibrations_model.tflite", "rb") as f:
    tflite_model = f.read()

# 🔹 Conversion en tableau de bytes C++ (pour Arduino)
hex_array = ", ".join("0x{:02x}".format(c) for c in tflite_model)

cpp_code = f"""
#ifndef VIBRATIONS_MODEL_H
#define VIBRATIONS_MODEL_H

alignas(8) const unsigned char vibrations_model_tflite[] = {{
    {hex_array}
}};
const int vibrations_model_tflite_len = {len(tflite_model)};

#endif  // VIBRATIONS_MODEL_H
"""

# 🔹 Sauvegarde du fichier C++ pour Arduino
with open("vibrations_model.h", "w") as f:
    f.write(cpp_code)

print("\n✅ Modèle converti en C++ : vibrations_model.h")
