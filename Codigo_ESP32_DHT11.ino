#define MONITOR_SERIAL Serial
#define RADAR_SERIAL Serial1
#define RADAR_RX_PIN 16
#define RADAR_TX_PIN 17

#include <WiFi.h>
#include <PubSubClient.h>
#include <WiFiClientSecure.h>
#include "DHT.h"
#include <time.h>
#include <ld2410.h>
#define DHTPIN 4 // Pin donde está conectado el sensor DHT11
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

ld2410 radar;

uint32_t lastReading = 0;
bool radarConnected = false;
const int ledPin = 5; // Pin del LED

// Configuración WiFi
const char* ssid = "Lucas_2.4";
const char* password = "Bender1234";

// Configuración MQTT
const char* mqtt_server = "z3ef5889.ala.us-east-1.emqxsl.com"; // Servidor MQTT
const int mqtt_port = 8883; // Puerto MQTT, para conexiones seguras
const char* mqtt_user = "nano1";
const char* mqtt_password = "nano1";

// Variables MQTT dinámicas
String macAddress;
String configTopic;
String roomNumber = "";

String mqtt_topic = "";
String mqtt_topic_temp = "";
String mqtt_topic_pres = "";
String mqtt_topic_moving = "";

WiFiClientSecure espClient; // Use WiFiClientSecure for secure connections
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando a ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi conectado");
  Serial.println("Dirección IP: ");
  Serial.println(WiFi.localIP());

  // Obtener dirección MAC y configurar el tópico de configuración
  macAddress = WiFi.macAddress();
  macAddress.replace(":", "");
  configTopic = "config/" + macAddress;
}

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (unsigned int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.print("Mensaje recibido [");
  Serial.print(topic);
  Serial.print("]: ");
  Serial.println(message);

  String topicStr = String(topic);

  if (topicStr == configTopic) {
    // Hemos recibido el número de sala
    roomNumber = message;
    Serial.print("Número de sala asignado: ");
    Serial.println(roomNumber);

    // Actualizar los tópicos MQTT
    mqtt_topic = roomNumber;
    mqtt_topic_temp = roomNumber + "/temp";
    mqtt_topic_pres = roomNumber + "/pres";
    mqtt_topic_moving = roomNumber + "/mov";

    // Suscribirse al tópico de la sala para controlar el LED
    client.subscribe(mqtt_topic.c_str());

  } else if (topicStr == mqtt_topic && roomNumber != "") {
    // Manejar mensajes para encender/apagar el LED
    if (message == "ON") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED encendido");
    } else if (message == "OFF") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED apagado");
    } else {
      // Puedes manejar otros comandos aquí si es necesario
      Serial.println("Comando no reconocido");
    }
  } else {
    // Manejar otros tópicos si es necesario
    Serial.println("Mensaje recibido en un tópico no manejado");
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Intentando conexión MQTT...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str(), mqtt_user, mqtt_password)) {
      Serial.println("Conectado al broker MQTT");

      // Suscribirse al tópico de configuración
      client.subscribe(configTopic.c_str());

      // Publicar la dirección MAC en el tópico de configuración
      client.publish(configTopic.c_str(), macAddress.c_str());

      // Si ya tenemos el número de sala, suscribirse al tópico de la sala
      if (roomNumber != "") {
        client.subscribe(mqtt_topic.c_str());
      }
    } else {
      Serial.print("Fallo, rc=");
      Serial.print(client.state());
      Serial.println(" intentando de nuevo en 5 segundos");
      delay(5000);
    }
  }
}

void setDateTime() {
  // Ajusta el desfase horario a UTC-3 (Chile) y maneja horario de verano
  const long gmtOffset_sec = -3 * 3600; // Offset para Chile (UTC-3)
  const int daylightOffset_sec = 3600; // Ajuste para horario de verano, si aplica

  configTime(gmtOffset_sec, daylightOffset_sec, "pool.ntp.org", "time.nist.gov");
  Serial.print("Esperando sincronización de tiempo NTP: ");
  time_t now = time(nullptr);
  while (now < 8 * 3600 * 2) { // Espera a que se sincronice la hora
    delay(100);
    Serial.print(".");
    now = time(nullptr);
  }
  Serial.println();
  struct tm timeinfo;
  gmtime_r(&now, &timeinfo);
  Serial.printf("%s", asctime(&timeinfo));
}

void setup(void) {
  Serial.begin(115200); // Iniciar monitor serie
  setup_wifi();

  espClient.setInsecure(); // Usar para conexiones TLS sin certificado cargado (no recomendado para producción)
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);

  reconnect(); // Conectar al broker MQTT

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // LED apagado al inicio

  dht.begin(); // Inicializa el sensor DHT
  setDateTime(); // Sincronizar la hora al inicio
  MONITOR_SERIAL.begin(115200); // Feedback en el monitor serie

  // Configurar el radar LD2410
  #if defined(ESP32)
    RADAR_SERIAL.begin(256000, SERIAL_8N1, RADAR_RX_PIN, RADAR_TX_PIN); // UART para el radar
  #elif defined(__AVR_ATmega32U4__)
    RADAR_SERIAL.begin(256000); // UART para el radar
  #endif
  delay(500);
  MONITOR_SERIAL.print(F("\nConectar LD2410 radar TX a GPIO:"));
  MONITOR_SERIAL.println(RADAR_RX_PIN);
  MONITOR_SERIAL.print(F("Conectar LD2410 radar RX a GPIO:"));
  MONITOR_SERIAL.println(RADAR_TX_PIN);
  MONITOR_SERIAL.print(F("Inicializando sensor radar LD2410: "));
  if (radar.begin(RADAR_SERIAL)) {
    MONITOR_SERIAL.println(F("OK"));
    MONITOR_SERIAL.print(F("Versión de firmware LD2410: "));
    MONITOR_SERIAL.print(radar.firmware_major_version);
    MONITOR_SERIAL.print('.');
    MONITOR_SERIAL.print(radar.firmware_minor_version);
    MONITOR_SERIAL.print('.');
    MONITOR_SERIAL.println(radar.firmware_bugfix_version, HEX);
  } else {
    MONITOR_SERIAL.println(F("no conectado"));
  }
}

void send_data() {
  static unsigned long lastMsg = 0;
  unsigned long now = millis();
  if (now - lastMsg > 5000) {
    lastMsg = now;

    if (roomNumber != "") {
      float temperature = dht.readTemperature(); // Lee la temperatura del DHT22

      // Verificar si la lectura fue exitosa
      if (isnan(temperature)) {
        Serial.println("Error al leer del sensor DHT");
      } else {
        // Obtener la hora actual
        time_t nowTime = time(nullptr);
        struct tm timeinfo;
        localtime_r(&nowTime, &timeinfo);

        // Formatear la fecha y hora
        char timeString[64];
        strftime(timeString, sizeof(timeString), "%Y-%m-%d %H:%M:%S", &timeinfo);

        // Crear el mensaje para publicar
        String message = String(temperature);
        Serial.println("Publicando temperatura: " + message);

        // Publicar la temperatura al tópico MQTT
        client.publish(mqtt_topic_temp.c_str(), message.c_str());
      }
    }
  }

  radar.read();
  if (radar.isConnected() && millis() - lastReading > 5000 && roomNumber != "") { // Reportar cada 5000ms
    lastReading = millis();
    if (radar.presenceDetected()) {
      if (radar.stationaryTargetDetected()) {
        Serial.print(F("Objetivo estacionario: "));
        Serial.print(radar.stationaryTargetDistance());
        Serial.print(F("cm energía:"));
        Serial.print(radar.stationaryTargetEnergy());
        Serial.print(' ');
        // Crear un String para almacenar la información
        String pres = "Stationary target: " + String(radar.stationaryTargetDistance()) + " cm\n";
        pres += "Energy: " + String(radar.stationaryTargetEnergy()) + "\n";
        // Publicarlo en el tópico MQTT 
        client.publish(mqtt_topic_pres.c_str(), pres.c_str());
      }
      if (radar.movingTargetDetected()) {
        Serial.print(F("Objetivo en movimiento: "));
        Serial.print(radar.movingTargetDistance());
        Serial.print(F("cm energía:"));
        Serial.print(radar.movingTargetEnergy());
        // Crear un String para almacenar la información
        String message = "Moving target: " + String(radar.movingTargetDistance()) + " cm\n";
        message += "Energy: " + String(radar.movingTargetEnergy()) + "\n";

        // Imprimir el mensaje en el Serial Monitor
        Serial.print(message);

        // Publicarlo en el tópico MQTT 
        client.publish(mqtt_topic_moving.c_str(), message.c_str());
      }
      Serial.println();
    } else {
      client.publish(mqtt_topic_pres.c_str(), "No target");
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  send_data();
}
