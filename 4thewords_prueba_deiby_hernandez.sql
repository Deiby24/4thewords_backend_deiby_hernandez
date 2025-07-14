
CREATE DATABASE IF NOT EXISTS 4thewords_prueba_deiby_hernandez CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE 4thewords_prueba_deiby_hernandez;


CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


CREATE TABLE province (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE canton (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    province_id INT NOT NULL,
    FOREIGN KEY (province_id) REFERENCES province(id)
);

CREATE TABLE district (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    canton_id INT NOT NULL,
    FOREIGN KEY (canton_id) REFERENCES canton(id)
);


CREATE TABLE legend (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    image_url VARCHAR(1000),
    description VARCHAR(1000) NOT NULL,
    category_id INT NOT NULL,
    district_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (district_id) REFERENCES district(id)
);


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


INSERT INTO category (name) VALUES
('Leyendas Urbanas'),
('Mitos Precolombinos'),
('Relatos Fantásticos'),
('Historias Campesinas');


INSERT INTO province (name) VALUES
('San José'),
('Alajuela'),
('Cartago');


INSERT INTO canton (name, province_id) VALUES
('Central', 1),
('Escazú', 1),
('Alajuela', 2),
('Grecia', 2),
('Cartago', 3);


INSERT INTO district (name, canton_id) VALUES
('Carmen', 1),
('Merced', 1),
('San Rafael', 2),
('Tambor', 3),
('San Roque', 4),
('Occidental', 5),
('Oriental', 5);

INSERT INTO legend (title, image_url, description, category_id, district_id) VALUES
('La Llorona', NULL, 'Una mujer que llora por sus hijos en las noches.', 1, 1),
('El Cadejos', NULL, 'Perro espectral que protege o castiga.', 2, 1),
('La Segua', NULL, 'Mujer hermosa que se transforma en espectro.', 1, 2),
('La Carreta sin Bueyes', NULL, 'Carreta fantasmal que anuncia la muerte.', 2, 3),
('El Padre sin Cabeza', NULL, 'Cura decapitado que deambula por caminos.', 3, 3),
('La Tulevieja', NULL, 'Espíritu de una madre castigada.', 3, 4),
('El Duende', NULL, 'Ser pequeño que confunde a los niños.', 3, 4),
('El Silbón', NULL, 'Alma en pena que silba antes de atacar.', 1, 5),
('La Piedra del Diablo', NULL, 'Piedra con marcas infernales.', 2, 6),
('El Jinete sin Cabeza', NULL, 'Caballero espectral sin cabeza.', 1, 1),
('El Cadejo Blanco', NULL, 'Versión buena del cadejo.', 2, 2),
('El Tesoro Encantado', NULL, 'Tesoro protegido por fuerzas mágicas.', 3, 2),
('La Novia Fantasma', NULL, 'Espíritu de una novia abandonada.', 1, 3),
('La Dama Tapada', NULL, 'Mujer con velo que castiga infieles.', 2, 4),
('El Sombrerón', NULL, 'Enano con sombrero enorme que enamora mujeres.', 3, 5),
('Los Cazadores Malditos', NULL, 'Grupo de almas cazando eternamente.', 2, 6),
('El Pozo Maldito', NULL, 'Pozo donde se escuchan voces.', 3, 7),
('La Mano Peluda', NULL, 'Mano que aparece desde la oscuridad.', 1, 1),
('El Monje Errante', NULL, 'Monje que carga cruz en penitencia.', 2, 2),
('El Gritón', NULL, 'Espíritu que grita en las noches.', 1, 3),
('El Toro del Diablo', NULL, 'Toro negro que aparece en la montaña.', 4, 4),
('La Sombra Blanca', NULL, 'Figura blanca que aparece al dormir.', 1, 5),
('La Mujer del Cerro', NULL, 'Mujer misteriosa que vive en el cerro.', 3, 6),
('El Niño de la Quebrada', NULL, 'Niño que aparece en ríos y quebradas.', 3, 7),
('El Árbol de los Colgados', NULL, 'Árbol donde aparecen cuerpos colgados.', 1, 2),
('La Casa de los Lamentos', NULL, 'Casa embrujada por una madre dolida.', 1, 3),
('El Viejo sin Ojos', NULL, 'Anciano ciego que guía a los perdidos.', 4, 5),
('El Fantasma del Ingenio', NULL, 'Trabajador que murió en accidente.', 4, 6),
('La Pila del Diablo', NULL, 'Pila donde el diablo se baña.', 2, 7),
('Los Pasos del Muerto', NULL, 'Pasos que se escuchan sin ver nada.', 1, 1),
('El Aullador', NULL, 'Ser que aúlla cuando alguien va a morir.', 3, 2),
('La Voz de la Cueva', NULL, 'Cueva de donde sale una voz atrapada.', 3, 3),
('El Espíritu del Puente', NULL, 'Puente donde se aparece una figura.', 1, 4);