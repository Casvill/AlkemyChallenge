DROP TABLE IF EXISTS tabla_general;
CREATE TABLE tabla_general
(
    id_tabla_general serial NOT NULL,
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    categoria VARCHAR(120),
    provincia VARCHAR(120),
    localidad VARCHAR(120),
    nombre VARCHAR(120),
    domicilio VARCHAR(120),
    codigo_postal VARCHAR(120),
    numero_de_telefono VARCHAR(120),
    mail VARCHAR(120),
    web VARCHAR(120),
    fecha_de_carga date,
    PRIMARY KEY (id_tabla_general)
);

DROP TABLE IF EXISTS cant_categoria;
CREATE TABLE cant_categoria
(
    id_cant_categoria serial NOT NULL,
    categoria VARCHAR(120),
    cantidad integer,
    fecha_de_carga date,
    PRIMARY KEY (id_cant_categoria)
);

DROP TABLE IF EXISTS cant_fuente;
CREATE TABLE cant_fuente
(
    id_cant_fuente serial NOT NULL,
    fuente VARCHAR(200),
    cantidad integer,
    fecha_de_carga date,
    PRIMARY KEY (id_cant_fuente)
);

DROP TABLE IF EXISTS cant_provincia_categoria;
CREATE TABLE cant_provincia_categoria
(
    id_cant_provincia_categoria serial NOT NULL,
    provincia VARCHAR(120),
    categoria VARCHAR(120),
    cantidad integer,
    fecha_de_carga date,
    PRIMARY KEY (id_cant_provincia_categoria)
);

DROP TABLE IF EXISTS salas_de_cine;
CREATE TABLE salas_de_cine
(
    id_salas_de_cine serial NOT NULL,
    provincia VARCHAR(120),
    cant_pantallas integer,
    cant_butacas integer,
    cant_espacios_incaa integer,
    fecha_de_carga date,
    PRIMARY KEY (id_salas_de_cine)
);