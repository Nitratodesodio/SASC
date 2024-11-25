INSERT INTO zona (nombre) VALUES
('Zona Norte'),
('Región Metropolitana'),
('Zona Sur');

INSERT INTO ciudad (nombre, cod_zona) VALUES
('Arica', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('Iquique', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('Calama', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('Antofagasta', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('Copiapó', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('La Serena', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('Valparaíso', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Norte')),
('Santiago', (SELECT cod_zona FROM zona WHERE nombre = 'Región Metropolitana')),
('Rancagua', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Curicó', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Talca', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Chillán', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Concepción-Talcahuano', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('San Pedro de la Paz', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Los Ángeles', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Temuco', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Valdivia', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Osorno', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Puerto Montt', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Coyhaique', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur')),
('Punta Arenas', (SELECT cod_zona FROM zona WHERE nombre = 'Zona Sur'));



INSERT INTO comuna (nombre, cod_ciudad) VALUES
-- Zona Norte
('Arica', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Arica')),
('Iquique', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Iquique')),
('Calama', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Calama')),
('Antofagasta', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Antofagasta')),
('Copiapó', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Copiapó')),
('La Serena', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'La Serena')),
('Valparaíso', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Valparaíso')),

-- Región Metropolitana
('Las Condes', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('Maipú', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('Renca', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('Ñuñoa', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('Santiago', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('Macul', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('La Granja', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),
('Puente Alto', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Santiago')),

-- Zona Sur
('Rancagua', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Rancagua')),
('Curicó', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Curicó')),
('Talca', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Talca')),
('Chillán', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Chillán')),
('Concepción', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Concepción-Talcahuano')),
('Talcahuano', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Concepción-Talcahuano')),
('San Pedro de la Paz', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'San Pedro de la Paz')),
('Los Ángeles', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Los Ángeles')),
('Temuco', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Temuco')),
('Valdivia', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Valdivia')),
('Osorno', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Osorno')),
('Puerto Montt', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Puerto Montt')),
('Coyhaique', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Coyhaique')),
('Punta Arenas', (SELECT cod_ciudad FROM ciudad WHERE nombre = 'Punta Arenas'));

INSERT INTO Estado (estado) VALUES
('Encendido'),
('Apagado'),
('Desconocido');

INSERT INTO Cargo (nombre) VALUES
('Jefe de Operaciones'),
('Director de Administración y Finanzas'),
('Coordinación'),
('Desconocido');


ALTER TABLE Tipo_Sensor
ALTER COLUMN nombre TYPE VARCHAR(50);


INSERT INTO Tipo_Sensor (nombre) VALUES
('Sensor Presencia LD2410c'),
('Sensor Temperatura y Humedad DHT22');


INSERT INTO Tipo_ac (nombre) VALUES
('Cassete'),
('Desconocido');


INSERT INTO Orientacion (orientacion) VALUES
('Norte'),
('Sur'),
('Este'),
('Oeste'),
('Noreste'),
('Noroeste'),
('Sureste'),
('Suroeste'),
('Desconocido');

INSERT INTO controlador (mac) VALUES
('a0:dd:6c:10:33:0c');

INSERT INTO Sensor (cod_tipo_sensor, cod_controlador)
VALUES (
       (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Presencia LD2410'), -- Subconsulta para obtener el código de tipo de sensor
    (SELECT cod_controlador FROM Controlador WHERE mac = 'a0:dd:6c:10:33:0c') -- Subconsulta para obtener el controlador relacionado con la MAC
),
(
       (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Temperatura y Humedad DHT22'),
    (SELECT cod_controlador FROM Controlador WHERE mac = 'a0:dd:6c:10:33:0c')
);

