create table cargo (
	cod_cargo smallserial,
	nombre varchar (40) not null,
	primary key (cod_cargo),
	constraint unique_nombre_cargo unique (nombre),
	constraint check_nombre_cargo check (trim(nombre) <> '')
);

create table zona (
	cod_zona smallserial,
	nombre varchar (20) not null,
	primary key (cod_zona),
	constraint unique_nombre_zona unique (nombre),
	constraint check_nombre_zona check (trim(nombre) <> '')
);

create table ciudad (
	cod_ciudad smallserial,
	nombre varchar (25) not null,
	cod_zona int not null,
	primary key (cod_ciudad),
	constraint fk_ciudad_zona foreign key (cod_zona)
		references zona (cod_zona)
		on delete cascade,
	constraint unique_nombre_ciudad unique (nombre),
	constraint check_nombre_ciudad check (trim(nombre) <> '')
);

create table comuna (
	cod_comuna smallserial,
	nombre varchar (20) not null,
	cod_ciudad int not null,
	primary key (cod_comuna),
	constraint fk_comuna_ciudad foreign key (cod_ciudad)
		references ciudad (cod_ciudad)
		on delete cascade,
	constraint unique_nombre_comuna unique (nombre),
	constraint check_nombre_comuna check (trim(nombre) <> '')
);

create table clima (
	cod_clima bigserial,
	fecha_hora timestamp not null,
	temperatura decimal (5,2) not null,
	humedad decimal (5,2) not null,
	cod_comuna int not null,
	primary key (cod_clima, fecha_hora),
	constraint fk_clima_comuna foreign key (cod_comuna)
		references comuna (cod_comuna)
		on delete cascade
);

create table sede (
	cod_sede smallserial,
	nombre varchar (30) not null,
	cod_zona int not null,
	cod_ciudad int not null,
	cod_comuna int not null,
	primary key (cod_sede),
	constraint fk_sede_comuna foreign key (cod_comuna)
		references comuna (cod_comuna)
		on delete cascade,
	constraint unique_nombre_sede unique (nombre),
	constraint check_nombre_sede check (trim(nombre) <> '')
);

create table edificio (
	cod_edificio serial,
	nombre varchar (30) not null,
	cod_sede int not null,
	primary key (cod_edificio),
	constraint fk_edificio_sede foreign key (cod_sede)
		references sede (cod_sede)
		on delete cascade,
	constraint unique_nombre_edificio unique (nombre),
	constraint check_nombre_edificio check (trim(nombre) <> '')
);

create table usuario (
	cod_usuario serial,
	rut varchar (10) unique,
	nombre varchar (40) not null,
	usuario varchar (30) unique,
	password varchar (255) not null,
	cod_cargo int not null,
	cod_sede int not null,
	primary key (cod_usuario),
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
	cod_controlador bigserial,
	mac varchar (30) not null,
	primary key (cod_controlador),
	constraint unique_mac_controlador unique (mac),
	constraint check_mac_controlador check (trim(mac) <> '')
);

create table tipo_sensor (
	cod_tipo_sensor smallserial,
	nombre varchar(20) not null,
	primary key (cod_tipo_sensor),
	constraint unique_nombre_tipo_sensor unique (nombre),
	constraint check_nombre_sensor check (trim(nombre) <> '')
);

create table sensor (
	cod_sensor serial,
	cod_tipo_sensor int not null,
	cod_controlador int not null,
	primary key (cod_sensor),
	constraint fk_sensor_tipo_sensor foreign key (cod_tipo_sensor)
		references tipo_sensor (cod_tipo_sensor)
		on delete cascade,
	constraint fk_sensor_controlador foreign key (cod_controlador)
		references controlador (cod_controlador)
		on delete cascade
);

create table lectura (
	cod_lectura bigserial,
	cod_sensor int not null,
	fecha_hora timestamp not null,
	primary key (cod_lectura),
	constraint fk_lectura_sensor foreign key (cod_sensor) 
		references sensor (cod_sensor)
		on delete cascade
);

create table valor_lectura (
	cod_valor bigserial,
	cod_lectura int not null,
	valor int not null,
	primary key (cod_valor),
	constraint fk_valor_lectura_lectura foreign key (cod_lectura) 
		references lectura (cod_lectura)
		on delete cascade
);

create table volumen (
	cod_vol serial,
	volumen decimal (5,2) not null,
	primary key (cod_vol),
	constraint unique_volumen_volumen unique (volumen),
	constraint check_volumen_volumen check (trim(volumen) <> '')
);

create table orientacion (
	cod_ori smallserial,
	orientacion varchar (10) not null,
	primary key (cod_ori),
	constraint unique_orientacion_orientacion unique (orientacion),
	constraint check_orientacion_orientacion check (trim(orientacion) <> '')
);

create table capacidad (
	cod_cap serial,
	cupo_estandar int not null,
	cupo_permitido int not null,
	primary key (cod_cap)
);

create table sala (
	cod_sala bigserial,
	numero int,
	cod_edificio int not null,
	cod_controlador int unique,
	cod_vol int not null,
	cod_ori int not null,
	cod_cap int not null,
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
		on delete cascade,
	constraint unique_numero_sala unique (numero),
	constraint check_numero_sala check (trim(numero) <> '')
);

create table tipo_ac (
	cod_tipo smallserial,
	nombre varchar (25) not null,
	primary key (cod_tipo),
	constraint unique_nombre_tipo_ac unique (nombre),
	constraint check_nombre_tipo_ac check (trim(nombre) <> '')
);

create table marca_ac (
	cod_marca smallserial,
	nombre varchar (10) not null,
	primary key (cod_marca),
	constraint unique_nombre_marca_ac unique (nombre)
);

create table modelo_ac (
	cod_modelo smallserial,
	modelo varchar (20) not null,
	primary key (cod_modelo),
	constraint unique_modelo_modelo_ac unique (modelo),
	constraint check_modelo_modelo_ac check (trim(modelo) <> '')
);

create table btu_tipo (
	cod_btu_tipo serial,
	tipo varchar (12) not null,
	primary key (cod_btu_tipo),
	constraint unique_tipo_btu_tipo unique (tipo),
	constraint check_tipo_btu_tipo check (trim(tipo) <> '')
);

create table btu_ac (
	cod_btu serial,
	valor int not null,
	cod_btu_tipo int not null,
	primary key (cod_btu),
	constraint fk_btu_ac_btu_tipo foreign key (cod_btu_tipo)
		references btu_tipo (cod_btu_tipo)
		on delete cascade,
	constraint check_valor_btu_ac check (trim(valor) <> '')
);

create table ac (
	cod_ac bigserial,
	cod_sala int not null,
	cod_tipo int not null,
	cod_marca int not null,
	cod_modelo int not null,
	cod_btu int not null,
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
	primary key (cod_mod),
	constraint unique_modalidad_modalidad unique (modalidad),
	constraint check_modalidad_modalidad check (trim(modalidad) <> '')
);

create table seccion (
	cod_sec serial,
	seccion varchar (20) not null,
	primary key (cod_sec),
	constraint unique_seccion_seccion unique (seccion),
	constraint check_seccion_seccion check (trim(seccion) <> '')
);

create table semestre (
	cod_sem smallserial,
	semestre int not null,
	primary key (cod_sem),
	constraint unique_semestre_semestre unique (semestre),
	constraint check_semestre_semestre check (trim(semestre) <> '')
);

create table asignatura (
	cod_asig bigserial,
	identificador varchar (15) not null,
	nombre varchar (100) not null,
	cod_mod int not null,
	cod_sem int not null,
	primary key (cod_asig),
	constraint fk_asignatura_modalidad foreign key (cod_mod)
		references modalidad (cod_mod)
		on delete cascade,
	constraint fk_asignatura_semestre foreign key (cod_sem)
		references semestre (cod_sem)
		on delete cascade,
	constraint unique_nombre_asignatura unique (nombre),
	constraint check_nombre_asignatura check (trim(nombre) <> '')
);

create table docente (
	cod_docente bigserial,
	rut varchar (10) not null,
	nombre varchar (30) not null,
	primer_apellido varchar (30) not null,
	segundo_apellido varchar (30) not null,
	primary key (cod_docente),
	constraint unique_rut_docente unique (rut),
	constraint check_rut_docente check (trim(rut) <> '')
);

create table docente_asignatura_seccion (
	cod_doc_asig_sec bigserial,
	cod_sec int not null,
	cod_docente int not null,
	cod_asig int not null,
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
	hora_inicio time not null,
	hora_fin time not null,
	primary key (bloque)
);

create table clase (
	cod_clase bigserial,
	cod_doc_asig_sec int not null,
	cod_sala int not null,
	sala_real int not null,
	bloque int not null,
	fecha date not null,
	primary key (cod_clase),
	constraint fk_clase_docente_asignatura_seccion foreign key (cod_doc_asig_sec)
		references docente_asignatura_seccion (cod_doc_asig_sec)
		on delete cascade,
	constraint fk_clase_sala foreign key (cod_sala)
		references sala (cod_sala)
		on delete cascade,
	constraint fk_clase_bloque_horario foreign key (bloque)
		references bloque_horario (bloque)
		on delete cascade
);
