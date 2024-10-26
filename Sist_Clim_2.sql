create table cargo (
	cod_cargo smallserial,
	nombre varchar (40) not null,
	primary key (cod_cargo)
);

create table zona (
	cod_zona smallserial,
	nombre varchar (20) not null,
	primary key (cod_zona)
);

create table ciudad (
	cod_ciudad smallserial,
	nombre varchar (25) not null,
	cod_zona int,
	primary key (cod_ciudad),
	constraint fk_ciudad_zona foreign key (cod_zona)
		references zona (cod_zona)
		on delete cascade
);

create table comuna (
	cod_comuna smallserial,
	nombre varchar (20) not null,
	cod_ciudad int,
	primary key (cod_comuna),
	constraint fk_comuna_ciudad foreign key (cod_ciudad)
		references ciudad (cod_ciudad)
		on delete cascade
);

create table clima (
	cod_clima bigserial,
	fecha_hora timestamp,
	temperatura decimal (5,2),
	humedad decimal (5,2),
	cod_comuna int,
	primary key (cod_clima, fecha_hora),
	constraint fk_clima_comuna foreign key (cod_comuna)
		references comuna (cod_comuna)
		on delete cascade
);

create table sede (
	cod_sede smallserial,
	nombre varchar (30) not null,
	cod_zona int,
	cod_ciudad int,
	cod_comuna int,
	primary key (cod_sede),
	constraint fk_sede_zona foreign key (cod_zona)
		references zona (cod_zona)
		on delete cascade,
	constraint fk_sede_ciudad foreign key (cod_ciudad)
		references ciudad (cod_ciudad)
		on delete cascade,
	constraint fk_sede_comuna foreign key (cod_comuna)
		references comuna (cod_comuna)
		on delete cascade
);

create table edificio (
	cod_edificio serial,
	nombre varchar (30) not null,
	cod_sede int,
	primary key (cod_edificio),
	constraint fk_edificio_sede foreign key (cod_sede)
		references sede (cod_sede)
		on delete cascade
);

create table usuario (
	cod_usuario serial,
	rut varchar (10) unique,
	nombre varchar (40) not null,
	usuario varchar (30) unique,
	password varchar (255) not null,
	cod_cargo int,
	cod_sede int,
	primary key (cod_usuario),
	constraint fk_usuario_cargo foreign key (cod_cargo)
		references cargo (cod_cargo)
		on delete cascade,
	constraint fk_usuario_sede foreign key (cod_sede)
		references sede (cod_sede)
		on delete cascade
);

create table tipo_sensor (
	cod_tipo_sensor smallserial,
	nombre varchar(20) not null,
	primary key (cod_tipo_sensor)
);

create table sensor (
	cod_sensor serial,
	cod_tipo_sensor int not null,
	primary key (cod_sensor),
	constraint fk_sensor_tipo_sensor foreign key (cod_tipo_sensor)
		references tipo_sensor (cod_tipo_sensor)
		on delete cascade
);

create table controlador (
	cod_controlador bigserial,
	mac varchar (30) not null,
	cod_sensor int,
	primary key (cod_controlador),
	unique (cod_controlador),
	foreign key (cod_sensor)
		references sensor (cod_sensor)
);

create table lectura_sensor (
	cod_lectura bigserial,
	cod_sensor int not null,
	fecha_hora timestamp not null,
	temperatura decimal (5,2),
	humedad decimal (5,2),
	ruido decimal (5,2),
	presencia boolean,
	co2 decimal (5,2),
	primary key (cod_lectura),
	constraint fk_lectura_sensor_sensor foreign key (cod_sensor)
		references sensor (cod_sensor)
		on delete cascade
);

create table volumen (
	cod_vol serial,
	volumen decimal (5,2) not null,
	primary key (cod_vol)
);

create table orientacion (
	cod_ori smallserial,
	orientacion varchar (10) not null,
	primary key (cod_ori)
);

create table capacidad (
	cod_cap serial,
	cupo_estandar int not null,
	cupo_permitido int not null,
	primary key (cod_cap)
);

create table sala (
	cod_sala bigserial,
	numero int unique,
	cod_edificio int,
	cod_sede int,
	cod_controlador int unique,
	cod_vol int,
	cod_ori int,
	cod_cap int,
	primary key (cod_sala),
	constraint fk_sala_edificio foreign key (cod_edificio)
		references edificio (cod_edificio)
		on delete cascade,
	constraint fk_sala_controlador foreign key (cod_controlador)
		references controlador (cod_controlador)
		on delete cascade,
	constraint fk_sala_volumen foreign key (cod_vol)
		references volumen (cod_vol)
		on delete cascade,
	constraint fk_sala_orientacion foreign key (cod_ori)
		references orientacion (cod_ori)
		on delete cascade,
	constraint fk_sala_capacidad foreign key (cod_cap)
		references capacidad (cod_cap)
		on delete cascade
);
----------------------------------

create table tipo_ac (
	cod_tipo smallserial,
	nombre varchar (25) not null,
	primary key (cod_tipo)
);

create table marca_ac (
	cod_marca smallserial,
	nombre varchar (10) not null,
	primary key (cod_marca)
);

create table modelo_ac (
	cod_modelo smallserial,
	modelo varchar (20) not null,
	primary key (cod_modelo)
);

create table btu_tipo (
	cod_btu_tipo serial,
	tipo varchar (12) not null,
	primary key (cod_btu_tipo)
);

create table btu_ac (
	cod_btu serial,
	valor int not null,
	cod_btu_tipo int,
	primary key (cod_btu),
	constraint fk_btu_ac_btu_tipo foreign key (cod_btu_tipo)
		references btu_tipo (cod_btu_tipo)
		on delete cascade
);

create table ac (
	cod_ac bigserial,
	cod_sala int,
	cod_tipo int,
	cod_marca int,
	cod_modelo int,
	cod_btu int,
	primary key (cod_ac),
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
		on delete cascade,
	constraint fk_ac_btu_ac foreign key (cod_btu)
		references btu_ac(cod_btu)
		on delete cascade
);

create table modalidad (
	cod_mod smallserial,
	modalidad varchar (20) not null,
	primary key (cod_mod)
);

create table seccion (
	cod_sec serial,
	seccion varchar (20) not null,
	primary key (cod_sec)
);

create table semestre (
	cod_sem smallserial,
	semestre int not null,
	primary key (cod_sem)
);

create table asignatura (
	cod_asig bigserial,
	identificador varchar (15) not null,
	nombre varchar (100) not null,
	cod_mod int,
	cod_sem int,
	primary key (cod_asig),
	constraint fk_asignatura_modalidad foreign key (cod_mod)
		references modalidad (cod_mod)
		on delete cascade,
	constraint fk_asignatura_semestre foreign key (cod_sem)
		references semestre (cod_sem)
		on delete cascade
);

create table docente (
	cod_docente bigserial,
	rut varchar (10) unique,
	nombre varchar (30) not null,
	primer_apellido varchar (30) not null,
	segundo_apellido varchar (30) not null,
	primary key (cod_docente)
);

create table docente_asignatura_seccion (
	cod_doc_asig_sec bigserial,
	cod_sec int,
	cod_docente int,
	cod_asig int,
	primary key (cod_doc_asig_sec),
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
	bloque smallserial,
	hora_inicio time,
	hora_fin time,
	primary key (bloque)
);

create table clase (
	cod_clase bigserial,
	cod_asig int,
	cod_sala int,
	sala_real int not null,
	bloque int ,
	primary key (cod_clase),
	constraint fk_clase_asignatura foreign key (cod_asig)
		references asignatura (cod_asig)
		on delete cascade,
	constraint fk_clase_sala foreign key (cod_sala)
		references sala (cod_sala)
		on delete cascade,
	constraint fk_clase_bloque_horario foreign key (bloque)
		references bloque_horario (bloque)
		on delete cascade
);




