CREATE DATABASE IF NOT EXISTS practica_servicios_tecnicos;
USE practica_servicios_tecnicos;

CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    correo VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    telefono VARCHAR(15)
);

-- Registros de prueba
INSERT INTO usuario (nombre, correo, password, telefono) 
VALUES ('admin', 'admin@ejemplo.com', '12345', '5551234567')
ON DUPLICATE KEY UPDATE nombre=nombre;

INSERT INTO usuario (nombre, correo, password, telefono) 
VALUES ('alumno', 'alumno@ejemplo.com', '2026', '5557654321')
ON DUPLICATE KEY UPDATE nombre=nombre;

