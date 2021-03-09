-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-07-2020 a las 19:29:12
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bookflix`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuncio`
--

CREATE TABLE `anuncio` (
  `id` int(6) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `contenido` text NOT NULL,
  `fecha_de_publicacion` date NOT NULL DEFAULT current_timestamp(),
  `ruta` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `anuncio`
--

INSERT INTO `anuncio` (`id`, `titulo`, `contenido`, `fecha_de_publicacion`, `ruta`) VALUES
(2, '¡Nuevo libro de harry potter!', 'Hemos agregado al catálogo del libro un nuevo libro de Harry Popotter, ¿qué estas esperando para leerlo?.', '2020-05-16', '../static/anuncios/51Vjb2qJwzL._SX331_BO1,204,203,200_.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `id` int(6) NOT NULL,
  `nombre` text NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `autor`
--

INSERT INTO `autor` (`id`, `nombre`, `activo`) VALUES
(1, 'test author', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `capitulo`
--

CREATE TABLE `capitulo` (
  `id` int(6) NOT NULL,
  `libro_id` int(6) NOT NULL,
  `fecha_publicacion` date NOT NULL,
  `ruta` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `capitulo`
--

INSERT INTO `capitulo` (`id`, `libro_id`, `fecha_publicacion`, `ruta`) VALUES
(1, 1, '2020-01-01', '../static/pdf/test.pdf'),
(2, 2, '2020-01-01', '../static/pdf/test.pdf'),
(3, 2, '2020-01-01', '../static/pdf/test.pdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editorial`
--

CREATE TABLE `editorial` (
  `id` int(6) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `editorial`
--

INSERT INTO `editorial` (`id`, `nombre`, `activo`) VALUES
(1, 'test editorial', 1),
(3, 'alba', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favorito`
--

CREATE TABLE `favorito` (
  `id` int(6) NOT NULL,
  `libro_id` int(6) NOT NULL,
  `perfil_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `favorito`
--

INSERT INTO `favorito` (`id`, `libro_id`, `perfil_id`) VALUES
(1, 1, 1),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id` int(6) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id`, `nombre`, `activo`) VALUES
(1, 'Drama', 1),
(2, 'horror', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `leido`
--

CREATE TABLE `leido` (
  `id` int(6) NOT NULL,
  `libro_id` int(6) NOT NULL,
  `perfil_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `leido`
--

INSERT INTO `leido` (`id`, `libro_id`, `perfil_id`) VALUES
(2, 1, 2),
(3, 1, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `leyendo`
--

CREATE TABLE `leyendo` (
  `id` int(6) NOT NULL,
  `libro_id` int(6) NOT NULL,
  `capitulo_id` int(6) NOT NULL,
  `perfil_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `leyendo`
--

INSERT INTO `leyendo` (`id`, `libro_id`, `capitulo_id`, `perfil_id`) VALUES
(1, 1, 1, 1),
(2, 2, 3, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `id` int(6) NOT NULL,
  `nombre` text NOT NULL,
  `isbn` varchar(100) NOT NULL,
  `fecha_publicacion` date NOT NULL,
  `fecha_vencimiento` date,
  `ruta_img` text NOT NULL,
  `sinopsis` text NOT NULL,
  `editorial` int(6) NOT NULL,
  `genero` int(6) NOT NULL,
  `autor` int(6) NOT NULL,
  `completo` tinyint(1) NOT NULL DEFAULT 0,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`id`, `nombre`, `isbn`, `fecha_publicacion`, `fecha_vencimiento`, `ruta_img`, `sinopsis`, `editorial`, `genero`, `autor`, `completo`, `activo`) VALUES
(1, 'test.pdf', '1234', '2010-01-01', '2021-01-01', '../static/pdf/test.jpg', 'test', 1, 1, 1, 0, 1),
(2, 'test por capitulos', '12346', '2010-01-01', '2021-01-01', '../static/pdf/test.jpg', 'test', 1, 1, 1, 0, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfiles`
--

CREATE TABLE `perfiles` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `foto` varchar(50) NOT NULL,
  `id_usuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `perfiles`
--

INSERT INTO `perfiles` (`id`, `nombre`, `foto`, `id_usuario`) VALUES
(1, 'juan', '../../static/img/img1.png', 2),
(2, 'hugo', '../../static/img/img2.png', 2),
(3, 'dai', '../../static/img/img3.png', 3),
(4, 'geronimo', '../../static/img/img4.png', 3),
(5, 'leandro', '../../static/img/img5.png', 2),
(7, 'maria', '../../static/img/img1.png', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plan`
--

CREATE TABLE `plan` (
  `id` int(6) NOT NULL,
  `nombre` text NOT NULL,
  `precio` float NOT NULL,
  `perfiles_max` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `plan`
--

INSERT INTO `plan` (`id`, `nombre`, `precio`, `perfiles_max`) VALUES
(1, 'basico', 250, 2),
(2, 'familiar', 400, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reseña`
--

CREATE TABLE `reseña` (
  `id` int(10) NOT NULL,
  `perfil_id` int(11) NOT NULL,
  `libro_id` int(11) NOT NULL,
  `calificacion` tinyint(4) NOT NULL,
  `comentario` text NOT NULL,
  `spoiler` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reseña`
--

INSERT INTO `reseña` (`id`, `perfil_id`, `libro_id`, `calificacion`, `comentario`, `spoiler`) VALUES
(1, 1, 1, 1, '1', 0),
(2, 6, 1, 2, '2', 0),
(3, 6, 2, 3, '3', 0),
(4, 4, 2, 4, '4', 0),
(5, 5, 1, 4, 'Sobresaliente, pero es una temática muy comercial y dejo un tanto que desear.', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `tarjetaNumero` varchar(30) NOT NULL,
  `tarjetaPin` varchar(10) NOT NULL,
  `tarjetaFechaDeExpiracion` date NOT NULL,
  `fecha_de_nacimiento` date NOT NULL,
  `plan_id` int(10) NOT NULL,
  `ultimo_pago` date DEFAULT NULL,
  `tarjeta_valida` tinyint(1) NOT NULL DEFAULT 1,
  `fecha_de_creacion` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `email`, `contraseña`, `tarjetaNumero`, `tarjetaPin`, `tarjetaFechaDeExpiracion`, `fecha_de_nacimiento`, `plan_id`, `fecha_de_creacion`) VALUES
(1, 'admin', 'admin', 'admin@gmail.com', 'admin', '100', '1212', '2020-05-31', '1999-08-30', 1, '2020-07-02'),
(2, 'hugo', 'contrera', 'hugo@gmail.com', '1234', '12345', '123', '2020-05-31', '1998-08-30', 1, '2020-07-02'),
(3, 'juan', 'perez', 'juanp@gmail.com', '1234', '4321', '1234', '2020-05-29', '1999-08-20', 1, '2020-07-02'),
(4, 'julia', 'perez', 'juli@gmail.com', '1234', '1212', '1222', '2020-05-30', '1999-08-30', 1, '2020-07-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vista_previa`
--

CREATE TABLE `vista_previa` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text NOT NULL,
  `video` varchar(50) NOT NULL,
  `pdf` varchar(50) NOT NULL,
  `imagen` varchar(50) NOT NULL,
  `fecha_de_publicacion` date NOT NULL,
  `activa` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vista_previa`
--

INSERT INTO `vista_previa` (`id`, `nombre`, `descripcion`, `video`, `pdf`, `imagen`, `fecha_de_publicacion`, `activa`) VALUES
(1, 'vista1', 'Esta es la descripcion de la vista 1', 'www.youtube.com', 'leer', 'hola', '2020-06-05', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `capitulo`
--
ALTER TABLE `capitulo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `editorial`
--
ALTER TABLE `editorial`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `favorito`
--
ALTER TABLE `favorito`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `leido`
--
ALTER TABLE `leido`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `leyendo`
--
ALTER TABLE `leyendo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `perfiles`
--
ALTER TABLE `perfiles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `plan`
--
ALTER TABLE `plan`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `reseña`
--
ALTER TABLE `reseña`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vista_previa`
--
ALTER TABLE `vista_previa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `capitulo`
--
ALTER TABLE `capitulo`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `editorial`
--
ALTER TABLE `editorial`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `favorito`
--
ALTER TABLE `favorito`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `leido`
--
ALTER TABLE `leido`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `leyendo`
--
ALTER TABLE `leyendo`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `perfiles`
--
ALTER TABLE `perfiles`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `plan`
--
ALTER TABLE `plan`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `reseña`
--
ALTER TABLE `reseña`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `vista_previa`
--
ALTER TABLE `vista_previa`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
