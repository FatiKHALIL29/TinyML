#include <Arduino_LSM9DS1.h> 
#include <TensorFlowLite.h>   
#include "vibrations_model.h" 

#include <tensorflow/lite/micro/all_ops_resolver.h>
#include <tensorflow/lite/micro/micro_error_reporter.h>
#include <tensorflow/lite/micro/micro_interpreter.h>
#include <tensorflow/lite/schema/schema_generated.h>
#include <tensorflow/lite/version.h>

const int tensor_arena_size = 2 * 1024;  // Taille du tampon de mémoire alloué pour TensorFlow Lite
uint8_t tensor_arena[tensor_arena_size];

tflite::MicroErrorReporter error_reporter;  // Pour les messages d'erreur de TensorFlow Lite
tflite::AllOpsResolver resolver;  // Résolveur d'opérations TensorFlow Lite
const tflite::Model* model = nullptr;  // Le modèle TFLite
tflite::MicroInterpreter* interpreter = nullptr;  // Interpréteur pour exécuter le modèle
TfLiteTensor* input = nullptr;  // Entrée du modèle
TfLiteTensor* output = nullptr;  // Sortie du modèle

void setup() {
    Serial.begin(115200);  // Initialisation de la communication série
    while (!Serial);

    if (!IMU.begin()) {
        Serial.println("Impossible d'initialiser l'IMU");
        while (1);  // Boucle infinie si l'IMU échoue à se configurer
    }

    Serial.println("IMU initialisé");

    // Chargement du modèle TensorFlow Lite
    model = tflite::GetModel(vibrations_model_tflite);
    if (model->version() != TFLITE_SCHEMA_VERSION) {
        Serial.println("Modèle incompatible");
        while (1);  // Boucle infinie si la version du modèle ne correspond pas
    }

    // Initialisation de l'interpréteur TensorFlow Lite
    static tflite::MicroInterpreter static_interpreter(
        model, resolver, tensor_arena, tensor_arena_size, &error_reporter);
    interpreter = &static_interpreter;

    // Allocation des tenseurs pour le modèle
    if (interpreter->AllocateTensors() != kTfLiteOk) {
        Serial.println("Erreur lors de l'allocation des tenseurs !");
        while (1);  // Boucle infinie si l'allocation échoue
    }

    Serial.println("Modèle chargé");
    input = interpreter->input(0);  // Récupération du premier tenseur d'entrée
    output = interpreter->output(0);  // Récupération du premier tenseur de sortie
}

void loop() {
    float x, y, z;

    // Lecture des données d'accélération de l'IMU
    if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(x, y, z);

        // Affichage des données d'accélération
        Serial.print("Accélération : ");
        Serial.print(x, 2);
        Serial.print(", ");
        Serial.print(y, 2);
        Serial.print(", ");
        Serial.println(z, 2);

        // Préparation des données d'entrée pour le modèle
        input->data.f[0] = x;
        input->data.f[1] = y;
        input->data.f[2] = z;

        // Exécution de l'inférence du modèle
        if (interpreter->Invoke() != kTfLiteOk) {
            Serial.println("Échec de l'inférence");
            return;  // Retour en cas d'échec
        }

        // Récupération de la prédiction
        float prediction = output->data.f[0];

        // Affichage du résultat du modèle
        Serial.print("Résultat du modèle : ");
        Serial.println(prediction, 4);

        // Interprétation du résultat
        if (prediction > 0.5) {
            Serial.println("État Stable.");
        } else {
            Serial.println("Forte Vibration");
        }
    }

    delay(500);  // Délai pour la prochaine itération
}
