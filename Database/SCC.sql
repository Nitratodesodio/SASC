CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

create table cargo (
	cod_cargo UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (40) not null,
	constraint unique_nombre_cargo unique (nombre),
	constraint check_nombre_cargo check (trim(nombre) <> '')
);

create table zona (
	cod_zona UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (20) not null,
	constraint unique_nombre_zona unique (nombre),
	constraint check_nombre_zona check (trim(nombre) <> '')
);

create table ciudad (
	cod_ciudad UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (50) not null,
	cod_zona UUID,
	constraint fk_ciudad_zona foreign key (cod_zona)
		references zona (cod_zona)
		on delete cascade,
	constraint unique_nombre_ciudad unique (nombre),
	constraint check_nombre_ciudad check (trim(nombre) <> '')
);

create table comuna (
	cod_comuna UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (20) not null,
	cod_ciudad UUID,
	constraint fk_comuna_ciudad foreign key (cod_ciudad)
		references ciudad (cod_ciudad)
		on delete cascade,
	constraint unique_nombre_comuna unique (nombre),
	constraint check_nombre_comuna check (trim(nombre) <> '')
);

create table clima (
	cod_clima UUID DEFAULT uuid_generate_v4() primary key,
	fecha_hora timestamp not null,
	temperatura decimal (5,2) not null,
	humedad decimal (5,2) not null,
	cod_comuna UUID,
	constraint fk_clima_comuna foreign key (cod_comuna)
		references comuna (cod_comuna)
		on delete cascade
);

create table sede (
	cod_sede UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (30) not null,
	cod_comuna UUID,
	constraint fk_sede_comuna foreign key (cod_comuna)
		references comuna (cod_comuna)
		on delete cascade,
	constraint unique_nombre_sede unique (nombre),
	constraint check_nombre_sede check (trim(nombre) <> '')
);

create table edificio (
	cod_edificio UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (30) not null,
	cod_sede UUID,
	constraint fk_edificio_sede foreign key (cod_sede)
		references sede (cod_sede)
		on delete cascade,
	constraint unique_nombre_edificio unique (nombre),
	constraint check_nombre_edificio check (trim(nombre) <> '')
);

create table usuario (
	cod_usuario UUID DEFAULT uuid_generate_v4() primary key,
	rut varchar (10) unique,
	nombre varchar (40) not null,
	usuario varchar (30) unique,
	password varchar (255) not null,
	cod_cargo UUID,
	cod_sede UUID,
	constraint fk_usuario_cargo foreign key (cod_cargo)
		references cargo (cod_cargo)
		on delete cascade,
	constraint fk_usuario_sede foreign key (cod_sede)
		references sede (cod_sede)
		on delete cascade,
	constraint unique_rut_usuario unique (rut),
	constraint check_rut_usuario check (trim(rut) <> ''),
	constraint check_nombre_usuario check (trim(nombre) <> ''),
	constraint check_usuario_usuario check (trim(usuario) <> ''),
	constraint check_password_usuario check (trim(password) <> '')
);

create table controlador (
	cod_controlador UUID DEFAULT uuid_generate_v4() primary key,
	mac varchar (50) not null,
	constraint unique_mac_controlador unique (mac),
	constraint check_mac_controlador check (trim(mac) <> '')
);

create table tipo_sensor (
	cod_tipo_sensor UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar(50) not null,
	constraint unique_nombre_tipo_sensor unique (nombre),
	constraint check_nombre_sensor check (trim(nombre) <> '')
);

create table sensor (
	cod_sensor UUID DEFAULT uuid_generate_v4() primary key,
	cod_tipo_sensor UUID,
	cod_controlador UUID,
	constraint fk_sensor_tipo_sensor foreign key (cod_tipo_sensor)
		references tipo_sensor (cod_tipo_sensor)
		on delete cascade,
	constraint fk_sensor_controlador foreign key (cod_controlador)
		references controlador (cod_controlador)
		on delete cascade
);

create table lectura (
	cod_lectura UUID DEFAULT uuid_generate_v4() primary key,
	cod_sensor UUID,
	valor float,
	fecha_hora timestamp not null,
	constraint fk_lectura_sensor foreign key (cod_sensor) 
		references sensor (cod_sensor)
		on delete cascade
);

create table orientacion (
	cod_ori UUID DEFAULT uuid_generate_v4() primary key,
	orientacion varchar (25) not null,
	constraint unique_orientacion_orientacion unique (orientacion),
	constraint check_orientacion_orientacion check (trim(orientacion) <> '')
);

create table sala (
	cod_sala UUID DEFAULT uuid_generate_v4() primary key,
	sala varchar(25) not null,
	capacidad int,
	cod_edificio UUID,
	cod_controlador UUID unique,
	volumen int not null,
	cod_ori UUID,
	constraint fk_sala_edificio foreign key (cod_edificio)
		references edificio (cod_edificio)
		on delete cascade,
	constraint fk_sala_controlador foreign key (cod_controlador)
		references controlador (cod_controlador)
		on delete cascade,
	constraint fk_sala_orientacion foreign key (cod_ori)
		references orientacion (cod_ori)
		on delete cascade,
	constraint unique_sala_sala unique (sala),
	constraint check_sala_sala check (trim(sala) <> '')
);

create table tipo_ac (
	cod_tipo UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (30) not null,
	constraint unique_nombre_tipo_ac unique (nombre),
	constraint check_nombre_tipo_ac check (trim(nombre) <> '')
);

create table marca_ac (
	cod_marca UUID DEFAULT uuid_generate_v4() primary key,
	nombre varchar (20) not null,
	constraint unique_nombre_marca_ac unique (nombre)
);

create table modelo_ac (
	cod_modelo UUID DEFAULT uuid_generate_v4() primary key,
	modelo varchar (25) not null,
	constraint unique_modelo_modelo_ac unique (modelo),
	constraint check_modelo_modelo_ac check (trim(modelo) <> '')
);

create table ac (
	cod_ac UUID DEFAULT uuid_generate_v4() primary key,
	cod_sala UUID,
	cod_tipo UUID,
	cod_marca UUID,
	cod_modelo UUID,
	btu int,
	constraint fk_ac_sala foreign key (cod_sala)
		references sala (cod_sala)
		on delete cascade,
	constraint fk_ac_tipo_ac foreign key (cod_tipo)
		references tipo_ac (cod_tipo)
		on delete cascade,
	constraint fk_ac_marca_ac foreign key (cod_marca)
		references marca_ac (cod_marca)
		on delete cascade,
	constraint fk_ac_modelo_ac foreign key (cod_modelo)
		references modelo_ac(cod_modelo)
		on delete cascade
);

create table estado (
	cod_estado UUID DEFAULT uuid_generate_v4() primary key,
	estado varchar (25) not null,
	constraint check_estado_estado_ac check (trim(estado) <> '')
);

create table estado_ac (
	cod_estado_ac UUID DEFAULT uuid_generate_v4() primary key,
	cod_estado UUID,
	cod_ac UUID,
	constraint fk_estado_ac_estado foreign key (cod_estado)
		references estado (cod_estado)
		on delete cascade,
	constraint fk_estado_ac_ac foreign key (cod_ac)
		references ac (cod_ac)
		on delete cascade
);

create table modalidad (
	cod_mod UUID DEFAULT uuid_generate_v4() primary key,
	modalidad varchar (25) not null,
	constraint unique_modalidad_modalidad unique (modalidad),
	constraint check_modalidad_modalidad check (trim(modalidad) <> '')
);

create table seccion (
	cod_sec UUID DEFAULT uuid_generate_v4() primary key,
	seccion varchar (50) not null,
	constraint unique_seccion_seccion unique (seccion),
	constraint check_seccion_seccion check (trim(seccion) <> '')
);

create table semestre (
	cod_sem UUID DEFAULT uuid_generate_v4() primary key,
	semestre varchar (20) not null,
	constraint unique_semestre_semestre unique (semestre)
);

create table asignatura (
	cod_asig UUID DEFAULT uuid_generate_v4() primary key,
	identificador varchar (30) not null,
	nombre varchar (100) not null,
	cod_mod UUID,
	cod_sem UUID,
	constraint fk_asignatura_modalidad foreign key (cod_mod)
		references modalidad (cod_mod)
		on delete cascade,
	constraint fk_asignatura_semestre foreign key (cod_sem)
		references semestre (cod_sem)
		on delete cascade,
	constraint unique_identificador_asignatura unique (identificador),
	constraint check_nombre_asignatura check (trim(nombre) <> '')
);

create table docente (
	cod_docente UUID DEFAULT uuid_generate_v4() primary key,
	rut varchar (10) not null,
	nombre varchar (30) not null,
	primer_apellido varchar (30) not null,
	segundo_apellido varchar (30) not null,
	constraint unique_rut_docente unique (rut),
	constraint check_rut_docente check (trim(rut) <> '')
);

create table docente_asignatura_seccion (
	cod_doc_asig_sec UUID DEFAULT uuid_generate_v4() primary key,
	cod_sec UUID,
	cod_docente UUID,
	cod_asig UUID,
	constraint fk_docente_asignatura_seccion_seccion foreign key (cod_sec)
		references seccion (cod_sec)
		on delete cascade,
	constraint fk_docente_asignatura_seccion_docente foreign key (cod_docente)
		references docente (cod_docente)
		on delete cascade,
	constraint fk_docente_asignatura_seccion_asignatura foreign key (cod_asig)
		references asignatura (cod_asig)
		on delete cascade
);

create table bloque_horario (
	bloque serial primary key,
	hora_inicio time not null,
	hora_fin time not null
);

create table clase (
	cod_clase UUID DEFAULT uuid_generate_v4() primary key,
	cod_doc_asig_sec UUID,
	cod_sala UUID,
	sala_real varchar (20),
	fecha date not null,
	constraint fk_clase_docente_asignatura_seccion foreign key (cod_doc_asig_sec)
		references docente_asignatura_seccion (cod_doc_asig_sec)
		on delete cascade,
	constraint fk_clase_sala foreign key (cod_sala)
		references sala (cod_sala)
		on delete cascade
);

create table bloque_clase(
	cod_bloque_clase UUID DEFAULT uuid_generate_v4() primary key,
	bloque int,
	cod_clase UUID,
	constraint fk_bloque_clase_bloque foreign key (bloque)
		references bloque_horario (bloque)
		on delete cascade,
	constraint fk_bloque_clase_clase foreign key (cod_clase)
		references clase (cod_clase)
		on delete cascade
);


