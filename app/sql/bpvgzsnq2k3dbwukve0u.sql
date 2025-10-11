-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Servidor: bpvgzsnq2k3dbwukve0u-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 11-10-2025 a las 20:48:13
-- Versión del servidor: 8.4.2-2
-- Versión de PHP: 8.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bpvgzsnq2k3dbwukve0u`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributos`
--

CREATE TABLE `atributos` (
  `IdAtributos` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributosXusuarios`
--

CREATE TABLE `atributosXusuarios` (
  `IdAtributosXusuarios` int NOT NULL,
  `IdUsuario` int NOT NULL,
  `IdAtributo` int NOT NULL,
  `Tipo` varchar(50) DEFAULT NULL,
  `Valor` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `IdModulos` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `modulos`
--

INSERT INTO `modulos` (`IdModulos`, `nombre`, `descripcion`) VALUES
(1, 'Ventas', 'Módulos de ventas'),
(2, 'Inventario', 'Módulo de inventario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloXrol`
--

CREATE TABLE `moduloXrol` (
  `IdModuloxRol` int NOT NULL,
  `IdRol` int NOT NULL,
  `IdModulo` int NOT NULL,
  `Estado` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `idRol` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`idRol`, `nombre`, `descripcion`) VALUES
(1, 'Administrador', 'Administrador'),
(2, 'Operador', 'Operador del sistema'),
(3, 'Auditor', 'Perfil de auditor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `idRol` int NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `edad` int NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `contrasena` varchar(20) NOT NULL,
  `fecha_update` datetime DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `idRol`, `nombre`, `apellido`, `cedula`, `edad`, `email`, `usuario`, `contrasena`, `fecha_update`, `fecha_creacion`, `estado`) VALUES
(1, 1, 'Ciro', 'Duran', '1234', 32, '', 'cduran', '1234556', NULL, NULL, ''),
(2, 1, 'string', 'string', 'string', 0, 'string', 'string', 'string', NULL, NULL, 'string'),
(3, 1, 'Carlos', 'Fernedez', '1234', 35, 'correo', 'cfernandez', '123', NULL, '2025-10-04 13:59:48', '1'),
(4, 1, 'Jairo', 'Ruiz', '6789', 80, 'rtyh@hjk.com', 'jruiz', '12t', NULL, '2025-10-04 15:20:07', 'Activo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributos`
--
ALTER TABLE `atributos`
  ADD PRIMARY KEY (`IdAtributos`);

--
-- Indices de la tabla `atributosXusuarios`
--
ALTER TABLE `atributosXusuarios`
  ADD PRIMARY KEY (`IdAtributosXusuarios`),
  ADD KEY `IdUsuario` (`IdUsuario`),
  ADD KEY `IdAtributo` (`IdAtributo`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`IdModulos`);

--
-- Indices de la tabla `moduloXrol`
--
ALTER TABLE `moduloXrol`
  ADD PRIMARY KEY (`IdModuloxRol`),
  ADD KEY `IdRol` (`IdRol`),
  ADD KEY `moduloXrol_ibfk_2` (`IdModulo`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`idRol`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_Usuarios_Rol` (`idRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `IdModulos` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `idRol` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `atributosXusuarios`
--
ALTER TABLE `atributosXusuarios`
  ADD CONSTRAINT `atributosXusuarios_ibfk_1` FOREIGN KEY (`IdUsuario`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `atributosXusuarios_ibfk_2` FOREIGN KEY (`IdAtributo`) REFERENCES `atributos` (`IdAtributos`);

--
-- Filtros para la tabla `moduloXrol`
--
ALTER TABLE `moduloXrol`
  ADD CONSTRAINT `moduloXrol_ibfk_1` FOREIGN KEY (`IdRol`) REFERENCES `rol` (`idRol`),
  ADD CONSTRAINT `moduloXrol_ibfk_2` FOREIGN KEY (`IdModulo`) REFERENCES `modulos` (`IdModulos`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `FK_Usuarios_Rol` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
