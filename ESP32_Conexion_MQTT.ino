#include <WiFi.h>
#include <PubSubClient.h>
#include <time.h>
#include <WiFiClientSecure.h>
#include <DHT.h>  // Biblioteca para el sensor DHT

#define DHTTYPE DHT11  
#define DHTPIN 4// Sensor temperatura
// Sensor de humedad
// Sensor Presencia
// Sensor Dioxido de carbono
#define LED_BUILTIN 5 // Rele que corta la corriente (Por ahora un LED)
DHT dht(DHTPIN, DHTTYPE);  // Crear una instancia del sensor DHT

// Valores de la red (Actualizar segun la red)
const char* ssid = "Lucas_2.4";
const char* password = "Bender1234";
const char* mqtt_server = "06bc99c0b5924c838684c04a7a0e45a1.s1.eu.hivemq.cloud"; // Servidor MQTT en HIVEMQ

WiFiClientSecure espClient;  //WiFiClientSecure para conexion TLS
PubSubClient client(espClient);

unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE (500) // Tamaño máximo del mensaje es de 500 caracteres.
char msg[MSG_BUFFER_SIZE];
float lastTemperature = NAN;
float lastHumidity = NAN;

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connectedo");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void setDateTime() {
  configTime(0, 0, "pool.ntp.org", "time.nist.gov");
  Serial.print("Waiting for NTP time sync: ");
  time_t now = time(nullptr);
  while (now < 8 * 3600 * 2) {
    delay(100);
    Serial.print(".");
    now = time(nullptr);
  }
  Serial.println();
  struct tm timeinfo;
  gmtime_r(&now, &timeinfo);
  Serial.printf("%s", asctime(&timeinfo));
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensaje recibido [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Convertir el payload a una cadena
  String receivedMessage = "";
  for (int i = 0; i < length; i++) {
    receivedMessage += (char)payload[i];
  }

  // Verificar si el mensaje recibido es "ENCIENDETE"
  if (receivedMessage == "ENCIENDETE") {
    digitalWrite(LED_BUILTIN, HIGH);  // Encender el LED
    Serial.println("LED encendido!");
  } else if (receivedMessage == "APAGATE") {
    digitalWrite(LED_BUILTIN, LOW);  // Apagar el LED
    Serial.println("LED apagado!");
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando MQTT...");
    String clientId = "ESP32Client";
    if (client.connect(clientId.c_str(), "Nitrato", "Hola1234")) {
      Serial.println("Conectado");

      // Suscribirse al tópico específico de la sala
      client.subscribe("sala/101");  // Cambia 101 por número de la sala que esta ESP32 controla
      if (client.subscribe("sala/101")) {
        Serial.println("Suscripción al tópico sala/101 exitosa");
    } else {
        Serial.println("Error al suscribirse al tópico sala/101");
    }
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}


void setup() {
  Serial.begin(9600);
  setup_wifi();
  setDateTime();
  dht.begin();  // Iniciar el sensor DHT

  pinMode(LED_BUILTIN, OUTPUT);  // Definir el pin del LED como salida
  digitalWrite(LED_BUILTIN, LOW);  // Apagar el LED por defecto

  espClient.setInsecure();
  client.setServer(mqtt_server, 8883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastMsg > 1000) { // Comprobar cada 1 segundos
    lastMsg = now;
    
    // Leer los datos del sensor DHT
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();
    if (isnan(temperature) || isnan(humidity)) {
      Serial.println("Failed to read from DHT sensor!");
      return;
    }
    
    // Verificar si la temperatura o la humedad han cambiado
    if (temperature != lastTemperature || humidity != lastHumidity) {
      // Actualizar los valores anteriores
      lastTemperature = temperature;
      lastHumidity = humidity;
      
     // Obtener la fecha y hora actual
      time_t now = time(nullptr);
      struct tm timeinfo;
      localtime_r(&now, &timeinfo);
      char dateTime[30];
      strftime(dateTime, sizeof(dateTime), "%Y-%m-%d %H:%M:%S", &timeinfo);
      
      // Publicar la temperatura, humedad y fecha/hora en el tópico MQTT
      snprintf(msg, MSG_BUFFER_SIZE, "Fecha y Hora: %s, Temperatura: %.2f °C, Humedad: %.2f %%", dateTime, temperature, humidity);
      Serial.print("Mensaje Publicado en sala/101/registro : ");
      Serial.println(msg);
      client.publish("sala/101/registro", msg);  // Publicar en el tópico testTopic (Reemplazar por sala/101/registro)
    }
  }
}
