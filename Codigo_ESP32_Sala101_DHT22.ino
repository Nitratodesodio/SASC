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
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

ld2410 radar;

uint32_t lastReading = 0;
bool radarConnected = false;
const int ledPin = 5; // Pin del LED


// Configuración WiFi
const char* ssid = "Lucas_2.4";
const char* password = "Bender1234";

// Configuración MQTT
const char* mqtt_server = "06bc99c0b5924c838684c04a7a0e45a1.s1.eu.hivemq.cloud"; // Servidor MQTT
const int mqtt_port = 8883; //Puerto MQTT, para conexiones seguras
const char* mqtt_user = "nano1";
const char* mqtt_password = "nano1";
const char* mqtt_topic = "101"; //Topico de la sala (Reemplazar por el numero de sala)
const char* mqtt_topic_temp = "101/temp"; // tópico para la temperatura
const char* mqtt_topic_pres = "101/pres"; // tópico para la temperatura
const char* mqtt_topic_moving = "101/mov";

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
}

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.print("Mensaje recibido [");
  Serial.print(topic);
  Serial.print("]: ");
  Serial.println(message);

  // Enciende o apaga el LED según el mensaje recibido
  if (message == "ON") {
    digitalWrite(ledPin, HIGH);
    Serial.println("LED encendido");
  } else if (message == "OFF") {
    digitalWrite(ledPin, LOW);
    Serial.println("LED apagado");
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Intentando conexión MQTT...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str(), mqtt_user, mqtt_password)) {
      Serial.println("Conectado al broker MQTT");
      client.subscribe(mqtt_topic);

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
  Serial.print("Waiting for NTP time sync: ");
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

void setup(void)
{
  setup_wifi();
  
  espClient.setInsecure(); // Se usa para conexiones TLS sin certificado cargado (no recomendado para producción)
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // LED apagado al inicio
  
  dht.begin(); // Inicializa el sensor DHT
  setDateTime(); // Sincronizar la hora al inicio
  MONITOR_SERIAL.begin(115200); //Feedback over Serial Monitor
  //radar.debug(MONITOR_SERIAL); //Uncomment to show debug information from the library on the Serial Monitor. By default this does not show sensor reads as they are very frequent.
  #if defined(ESP32)
    RADAR_SERIAL.begin(256000, SERIAL_8N1, RADAR_RX_PIN, RADAR_TX_PIN); //UART for monitoring the radar
  #elif defined(__AVR_ATmega32U4__)
    RADAR_SERIAL.begin(256000); //UART for monitoring the radar
  #endif
  delay(500);
  MONITOR_SERIAL.print(F("\nConnect LD2410 radar TX to GPIO:"));
  MONITOR_SERIAL.println(RADAR_RX_PIN);
  MONITOR_SERIAL.print(F("Connect LD2410 radar RX to GPIO:"));
  MONITOR_SERIAL.println(RADAR_TX_PIN);
  MONITOR_SERIAL.print(F("LD2410 radar sensor initialising: "));
  if(radar.begin(RADAR_SERIAL))
  {
    MONITOR_SERIAL.println(F("OK"));
    MONITOR_SERIAL.print(F("LD2410 firmware version: "));
    MONITOR_SERIAL.print(radar.firmware_major_version);
    MONITOR_SERIAL.print('.');
    MONITOR_SERIAL.print(radar.firmware_minor_version);
    MONITOR_SERIAL.print('.');
    MONITOR_SERIAL.println(radar.firmware_bugfix_version, HEX);
  }
  else
  {
    MONITOR_SERIAL.println(F("not connected"));
  }
}

void loop()
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Leer temperatura y humedad cada 5 segundos
  static unsigned long lastMsg = 0;
  unsigned long now = millis();
  if (now - lastMsg > 5000) {
    lastMsg = now;
    
    float temperature = dht.readTemperature(); // Lee la temperatura del DHT11

    // Verificar si la lectura fue exitosa
    if (isnan(temperature)) {
      Serial.println("Error al leer del sensor DHT");
    } else {
      // Obtener la hora actual
      time_t now = time(nullptr);
      struct tm timeinfo;
      localtime_r(&now, &timeinfo);

      // Formatear la fecha y hora
      char timeString[64];
      strftime(timeString, sizeof(timeString), "%Y-%m-%d %H:%M:%S", &timeinfo);

      // Crear el mensaje para publicar
      String message = String(timeString) + " - Temperatura: " + String(temperature);
      Serial.println("Publicando: " + message);

      // Publicar la temperatura y fecha/hora al tópico MQTT
      client.publish(mqtt_topic_temp, message.c_str());
    }
  }
  radar.read();
  if(radar.isConnected() && millis() - lastReading > 1000)  //Report every 1000ms
  {
    lastReading = millis();
    if(radar.presenceDetected())
    {
      if(radar.stationaryTargetDetected())
      {
        Serial.print(F("Stationary target: "));
        Serial.print(radar.stationaryTargetDistance());
        Serial.print(F("cm energy:"));
        Serial.print(radar.stationaryTargetEnergy());
        Serial.print(' ');
        // Crear un String para almacenar la información
        String pres = "Stationary target: " + String(radar.stationaryTargetDistance()) + "\n";
        pres += "cm energy: " + String(radar.stationaryTargetEnergy()) + "\n";
        // Publicarlo en el tópico MQTT 
        client.publish(mqtt_topic_pres, pres.c_str());
      }
      if(radar.movingTargetDetected())
      {
        Serial.print(F("Moving target: "));
        Serial.print(radar.movingTargetDistance());
        Serial.print(F("cm energy:"));
        Serial.print(radar.movingTargetEnergy());
        // Crear un String para almacenar la información
        String message = "Moving target: " + String(radar.movingTargetDistance()) + "\n";
        message += "cm energy: " + String(radar.movingTargetEnergy()) + "\n";

        // Imprimir el mensaje en el Serial Monitor
        Serial.print(message);

       // Publicarlo en el tópico MQTT 
       client.publish(mqtt_topic_moving, message.c_str());
     
      }
      Serial.println();
    }
    else
    {
      client.publish(mqtt_topic_pres,"No target");
    }
  }
}
