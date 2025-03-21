#include <Arduino_LSM9DS1.h>  // Librairie pour utiliser le capteur IMU

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Attend que la communication série soit prête

  // Initialise l'IMU
  if (!IMU.begin()) {
    Serial.println("Erreur : capteur IMU non détecté !");
    while (1);  // Bloque le programme en cas d'erreur
  }
  Serial.println("IMU initialisé avec succès !");
}

void loop() {
  float x, y, z;

  // Vérifie si des données d'accélération sont disponibles
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    // Envoie les valeurs sur le Serial Monitor, séparées par une virgule
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(z);
  }
  delay(100);  // Petite pause pour ne pas inonder le Serial Monitor
}

