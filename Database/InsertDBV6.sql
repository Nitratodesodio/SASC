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
('Administrador'),
('Jefe de Operaciones'),
('Director de Administración y Finanzas'),
('Coordinación'),
('Desconocido');

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

ALTER TABLE Tipo_Sensor
ALTER COLUMN nombre TYPE VARCHAR(50);

INSERT INTO sede (nombre, cod_comuna)
VALUES (
    'Santiago Sur',
    (SELECT cod_comuna FROM comuna WHERE nombre = 'Macul')
);


INSERT INTO edificio (nombre, cod_sede)
VALUES
    ('A', (SELECT cod_sede FROM sede WHERE nombre = 'Santiago Sur')),
    ('B', (SELECT cod_sede FROM sede WHERE nombre = 'Santiago Sur')),
    ('C', (SELECT cod_sede FROM sede WHERE nombre = 'Santiago Sur')),
    ('D', (SELECT cod_sede FROM sede WHERE nombre = 'Santiago Sur'));


insert into marca_ac (nombre) values ('Toshiba');
insert into marca_ac (nombre) values ('Haier');

insert into modelo_ac (modelo) values ('MMU-AP0271H');
insert into modelo_ac (modelo) values ('MMU-AP0361H');
insert into modelo_ac (modelo) values ('MMC-AP0361H');

INSERT INTO Tipo_Sensor (nombre) VALUES
('Sensor Presencia LD2410c'),
('Sensor Temperatura DHT22'),
('Sensor Humedad DHT22');


INSERT INTO controlador (mac) VALUES
('A0:DD:6C:10:33:0C'),
('A0:DD:6C:0F:DF:B0');


INSERT INTO Sensor (cod_tipo_sensor, cod_controlador)
VALUES (
    (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Presencia LD2410c'), -- Subconsulta para obtener el código de tipo de sensor
    (SELECT cod_controlador FROM Controlador WHERE mac = 'A0:DD:6C:10:33:0C') -- Subconsulta para obtener el controlador relacionado con la MAC
),
(
    (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Temperatura DHT22'),
    (SELECT cod_controlador FROM Controlador WHERE mac = 'A0:DD:6C:10:33:0C')
),
    (
    (SELECT cod_tipo_sensor FROM Tipo_sensor WHERE nombre = 'Sensor Humedad DHT22'),
    (SELECT cod_controlador FROM controlador WHERE mac = 'A0:DD:6C:10:33:0C')
    );

INSERT INTO Sensor (cod_tipo_sensor, cod_controlador)
VALUES 
    (
        (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Presencia LD2410c'),
        (SELECT cod_controlador FROM Controlador WHERE mac = 'A0:DD:6C:0F:DF:B0')
    ),
    (
        (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Temperatura DHT22'),
        (SELECT cod_controlador FROM Controlador WHERE mac = 'A0:DD:6C:0F:DF:B0')
    ),
    (
        (SELECT cod_tipo_sensor FROM Tipo_Sensor WHERE nombre = 'Sensor Humedad DHT22'),
        (SELECT cod_controlador FROM Controlador WHERE mac = 'A0:DD:6C:0F:DF:B0')
    );


INSERT INTO ac (cod_sala, cod_tipo, cod_marca, cod_modelo, btu)
VALUES 
    (
        (SELECT cod_sala FROM sala WHERE sala = '111'),
        (SELECT cod_tipo FROM tipo_ac WHERE nombre = 'Cassete'),
        (SELECT cod_marca FROM marca_ac WHERE nombre = 'Toshiba'),
        (SELECT cod_modelo FROM modelo_ac WHERE modelo = 'MMU-AP0271H'),
        36000
    ),
    (
        (SELECT cod_sala FROM sala WHERE sala = '112'),
        (SELECT cod_tipo FROM tipo_ac WHERE nombre = 'Cassete'),
        (SELECT cod_marca FROM marca_ac WHERE nombre = 'Toshiba'),
        (SELECT cod_modelo FROM modelo_ac WHERE modelo = 'MMU-AP0271H'),
        36000
    ),
    (
        (SELECT cod_sala FROM sala WHERE sala = '117'),
        (SELECT cod_tipo FROM tipo_ac WHERE nombre = 'Cassete'),
        (SELECT cod_marca FROM marca_ac WHERE nombre = 'Toshiba'),
        (SELECT cod_modelo FROM modelo_ac WHERE modelo = 'MMU-AP0361H'),
        36000
    ),
    (
        (SELECT cod_sala FROM sala WHERE sala = '118'),
        (SELECT cod_tipo FROM tipo_ac WHERE nombre = 'Cassete'),
        (SELECT cod_marca FROM marca_ac WHERE nombre = 'Toshiba'),
        (SELECT cod_modelo FROM modelo_ac WHERE modelo = 'MMU-AP0361H'),
        36000
    ),
    (
        (SELECT cod_sala FROM sala WHERE sala = '201'),
        (SELECT cod_tipo FROM tipo_ac WHERE nombre = 'Cassete'),
        (SELECT cod_marca FROM marca_ac WHERE nombre = 'Toshiba'),
        (SELECT cod_modelo FROM modelo_ac WHERE modelo = 'MMU-AP0361H'),
        36000
    ),
    (
        (SELECT cod_sala FROM sala WHERE sala = '202'),
        (SELECT cod_tipo FROM tipo_ac WHERE nombre = 'Cassete'),
        (SELECT cod_marca FROM marca_ac WHERE nombre = 'Toshiba'),
        (SELECT cod_modelo FROM modelo_ac WHERE modelo = 'MMU-AP0361H'),
        36000
    );

