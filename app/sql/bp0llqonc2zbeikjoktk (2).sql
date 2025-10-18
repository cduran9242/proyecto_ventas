-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Servidor: bp0llqonc2zbeikjoktk-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 18-10-2025 a las 05:46:47
-- Versión del servidor: 8.0.22-13
-- Versión de PHP: 8.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bp0llqonc2zbeikjoktk`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributos`
--

CREATE TABLE `atributos` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `estado_id` int NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributoXusuario`
--

CREATE TABLE `atributoXusuario` (
  `id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `atributo_id` int NOT NULL,
  `tipo` enum('texto','numero','booleano','fecha','json') NOT NULL,
  `valor` text,
  `estado_id` int NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Detalle_Pedidos`
--

CREATE TABLE `Detalle_Pedidos` (
  `IdDetalle_Pedidos` int NOT NULL,
  `IdPedido` int NOT NULL,
  `IdProducto` int NOT NULL,
  `Numero_Linea` int DEFAULT NULL,
  `Cantidad_solicitada` decimal(10,2) NOT NULL,
  `Cantidad_confirmada` decimal(10,2) DEFAULT NULL,
  `Precio_unitario` decimal(10,4) DEFAULT NULL,
  `Precio_Total` decimal(10,4) DEFAULT NULL,
  `Precio_Extrajero` decimal(10,4) DEFAULT NULL,
  `Precio_Total_extrajero` decimal(10,4) DEFAULT NULL,
  `Numero_Documento` varchar(50) DEFAULT NULL,
  `Tipo_Documento` varchar(50) DEFAULT NULL,
  `Estado_Siguiente` int NOT NULL,
  `Estado_Anterior` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Detalle_Wo`
--

CREATE TABLE `Detalle_Wo` (
  `Id_Detalle_WO` int NOT NULL,
  `IdWo` int NOT NULL,
  `IdPedido` int DEFAULT NULL,
  `IdProducto` int NOT NULL,
  `Cantidad_Solicitada` decimal(10,2) NOT NULL,
  `Cantidad_Producida` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Dimensiones_producto`
--

CREATE TABLE `Dimensiones_producto` (
  `IdDimensiones` int NOT NULL,
  `IdProducto` int NOT NULL,
  `Ancho` decimal(10,2) DEFAULT NULL,
  `Espesor` decimal(10,2) DEFAULT NULL,
  `Diametro_Interno` decimal(10,2) DEFAULT NULL,
  `Diametro_Externo` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Encabezado_Pedidos`
--

CREATE TABLE `Encabezado_Pedidos` (
  `IdPedido` int NOT NULL,
  `Tipo_Pedido` varchar(50) DEFAULT NULL,
  `IdCliente` int NOT NULL,
  `IdVendedor` int NOT NULL,
  `Moneda` varchar(10) DEFAULT NULL,
  `TRM` decimal(10,4) DEFAULT NULL,
  `OC_Cliente` varchar(50) DEFAULT NULL,
  `Condicion_pago` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE `estados` (
  `id` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`id`, `nombre`, `descripcion`, `created_at`, `updated_at`) VALUES
(1, 'Activo', 'Estado activo del registro', '2025-10-18 02:58:47', '2025-10-18 02:58:47'),
(2, 'Inactivo', 'Estado inactivo del registro', '2025-10-18 02:58:47', '2025-10-18 02:58:47'),
(3, 'Suspendido', 'Estado suspendido del registro', '2025-10-18 02:58:47', '2025-10-18 02:58:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Inventario`
--

CREATE TABLE `Inventario` (
  `Idinvnetario` int NOT NULL,
  `IdProducto` int NOT NULL,
  `Lote` varchar(50) DEFAULT NULL,
  `Cantidad_disponible` decimal(10,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `ruta` varchar(255) DEFAULT NULL,
  `estado_id` int NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `modulos`
--

INSERT INTO `modulos` (`id`, `nombre`, `descripcion`, `ruta`, `estado_id`, `created_at`, `updated_at`) VALUES
(1, 'Ventas', 'Modulo de ventas', '/ventas', 1, '2025-10-15 05:17:14', '2025-10-18 03:01:15'),
(2, 'Inventario', 'Modulo de inventario', '/inventario', 1, '2025-10-15 05:17:14', '2025-10-18 03:01:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloXrol`
--

CREATE TABLE `moduloXrol` (
  `id` int NOT NULL,
  `rol_id` int NOT NULL,
  `modulo_id` int NOT NULL,
  `permisos` json DEFAULT NULL,
  `estado_id` int NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Ordenes_Produccion`
--

CREATE TABLE `Ordenes_Produccion` (
  `IdWo` int NOT NULL,
  `Estado_Siguiente` varchar(50) DEFAULT NULL,
  `Estado_Anterior` varchar(50) DEFAULT NULL,
  `Fecha_Inicio` datetime DEFAULT NULL,
  `Fecha_Fin_Estimada` datetime DEFAULT NULL,
  `Fecha_Fin_Real` datetime DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Productos`
--

CREATE TABLE `Productos` (
  `IdProductos` int NOT NULL,
  `Codigo_producto` varchar(50) NOT NULL,
  `Nombre_Producto` varchar(150) NOT NULL,
  `Descripcion` text,
  `Categoria` varchar(50) DEFAULT NULL,
  `Unidad_medida` varchar(20) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `estado_id` int NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`, `descripcion`, `estado_id`, `created_at`, `updated_at`) VALUES
(1, 'Administrador', 'Admin del sistema', 1, '2025-10-15 05:13:52', '2025-10-18 03:01:59'),
(2, 'Operador', 'Operador del sistema', 1, '2025-10-15 05:13:52', '2025-10-18 03:01:59'),
(3, 'Auditor', 'Perfil del auditor', 1, '2025-10-15 05:13:52', '2025-10-18 03:01:59');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `nombres` varchar(150) NOT NULL,
  `apellidos` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `cedula` varchar(20) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `rol_id` int DEFAULT NULL,
  `estado_id` int NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombres`, `apellidos`, `email`, `telefono`, `cedula`, `contrasena`, `rol_id`, `estado_id`, `created_at`, `updated_at`) VALUES
(1, 'Andrés', 'Muñoz Púa', 'andres.munoz@gmail.com', '3001112233', '1023415678', 'admin_123', 1, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(2, 'Valentina', 'Gómez Rojas', 'valentina.gomez@gmail.com', '3012223344', '1009876543', 'admin_456', 1, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(3, 'Carlos', 'Pérez Díaz', 'carlos.perez@gmail.com', '3023334455', '1001234567', 'operador_789', 2, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(4, 'Laura', 'Martínez Ruiz', 'laura.martinez@gmail.com', '3034445566', '1025678901', 'auditor_159', 3, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(5, 'José', 'Torres Mejía', 'jose.torres@gmail.com', '3045556677', '1014582390', 'operador_753', 2, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(6, 'Sofía', 'López Castillo', 'sofia.lopez@gmail.com', '3056667788', '1037896542', 'auditor_951', 3, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(7, 'Ricardo', 'Mendoza Parra', 'ricardo.mendoza@gmail.com', '3067778899', '1057893214', 'admin_258', 1, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(8, 'María', 'Fernández Ortiz', 'maria.fernandez@gmail.com', '3078889900', '1046789321', 'operador_357', 2, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(9, 'Natalia', 'Suárez León', 'natalia.suarez@gmail.com', '3089990011', '1012349823', 'auditor_456', 3, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18'),
(10, 'Esteban', 'Cárdenas Mora', 'esteban.cardenas@gmail.com', '3090001122', '1098765432', 'operador_852', 2, 1, '2025-10-15 05:19:47', '2025-10-18 03:02:18');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributos`
--
ALTER TABLE `atributos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_atributos_estado` (`estado_id`);

--
-- Indices de la tabla `atributoXusuario`
--
ALTER TABLE `atributoXusuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`,`atributo_id`),
  ADD KEY `atributo_id` (`atributo_id`),
  ADD KEY `fk_atributoXusuario_estado` (`estado_id`);

--
-- Indices de la tabla `Detalle_Pedidos`
--
ALTER TABLE `Detalle_Pedidos`
  ADD PRIMARY KEY (`IdDetalle_Pedidos`),
  ADD KEY `IdPedido` (`IdPedido`),
  ADD KEY `IdProducto` (`IdProducto`);

--
-- Indices de la tabla `Detalle_Wo`
--
ALTER TABLE `Detalle_Wo`
  ADD PRIMARY KEY (`Id_Detalle_WO`),
  ADD KEY `IdWo` (`IdWo`),
  ADD KEY `IdPedido` (`IdPedido`),
  ADD KEY `IdProducto` (`IdProducto`);

--
-- Indices de la tabla `Dimensiones_producto`
--
ALTER TABLE `Dimensiones_producto`
  ADD PRIMARY KEY (`IdDimensiones`),
  ADD KEY `IdProducto` (`IdProducto`);

--
-- Indices de la tabla `Encabezado_Pedidos`
--
ALTER TABLE `Encabezado_Pedidos`
  ADD PRIMARY KEY (`IdPedido`),
  ADD KEY `IdVendedor` (`IdVendedor`);

--
-- Indices de la tabla `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `Inventario`
--
ALTER TABLE `Inventario`
  ADD PRIMARY KEY (`Idinvnetario`),
  ADD KEY `IdProducto` (`IdProducto`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `fk_modulos_estado` (`estado_id`);

--
-- Indices de la tabla `moduloXrol`
--
ALTER TABLE `moduloXrol`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rol_id` (`rol_id`,`modulo_id`),
  ADD KEY `modulo_id` (`modulo_id`),
  ADD KEY `fk_moduloXrol_estado` (`estado_id`);

--
-- Indices de la tabla `Ordenes_Produccion`
--
ALTER TABLE `Ordenes_Produccion`
  ADD PRIMARY KEY (`IdWo`);

--
-- Indices de la tabla `Productos`
--
ALTER TABLE `Productos`
  ADD PRIMARY KEY (`IdProductos`),
  ADD UNIQUE KEY `Codigo_producto` (`Codigo_producto`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `fk_roles_estado` (`estado_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `idx_usuario_rol` (`rol_id`),
  ADD KEY `fk_usuarios_estado` (`estado_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `atributos`
--
ALTER TABLE `atributos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `atributoXusuario`
--
ALTER TABLE `atributoXusuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Detalle_Pedidos`
--
ALTER TABLE `Detalle_Pedidos`
  MODIFY `IdDetalle_Pedidos` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Detalle_Wo`
--
ALTER TABLE `Detalle_Wo`
  MODIFY `Id_Detalle_WO` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Dimensiones_producto`
--
ALTER TABLE `Dimensiones_producto`
  MODIFY `IdDimensiones` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estados`
--
ALTER TABLE `estados`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `Inventario`
--
ALTER TABLE `Inventario`
  MODIFY `Idinvnetario` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `moduloXrol`
--
ALTER TABLE `moduloXrol`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Productos`
--
ALTER TABLE `Productos`
  MODIFY `IdProductos` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `atributoXusuario`
--
ALTER TABLE `atributoXusuario`
  ADD CONSTRAINT `atributoXusuario_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `atributoXusuario_ibfk_2` FOREIGN KEY (`atributo_id`) REFERENCES `atributos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Detalle_Pedidos`
--
ALTER TABLE `Detalle_Pedidos`
  ADD CONSTRAINT `Detalle_Pedidos_ibfk_1` FOREIGN KEY (`IdPedido`) REFERENCES `Encabezado_Pedidos` (`IdPedido`),
  ADD CONSTRAINT `Detalle_Pedidos_ibfk_2` FOREIGN KEY (`IdProducto`) REFERENCES `Productos` (`IdProductos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Detalle_Wo`
--
ALTER TABLE `Detalle_Wo`
  ADD CONSTRAINT `Detalle_Wo_ibfk_1` FOREIGN KEY (`IdWo`) REFERENCES `Ordenes_Produccion` (`IdWo`),
  ADD CONSTRAINT `Detalle_Wo_ibfk_2` FOREIGN KEY (`IdPedido`) REFERENCES `Encabezado_Pedidos` (`IdPedido`),
  ADD CONSTRAINT `Detalle_Wo_ibfk_3` FOREIGN KEY (`IdProducto`) REFERENCES `Productos` (`IdProductos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Dimensiones_producto`
--
ALTER TABLE `Dimensiones_producto`
  ADD CONSTRAINT `Dimensiones_producto_ibfk_1` FOREIGN KEY (`IdProducto`) REFERENCES `Productos` (`IdProductos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Encabezado_Pedidos`
--
ALTER TABLE `Encabezado_Pedidos`
  ADD CONSTRAINT `Encabezado_Pedidos_ibfk_1` FOREIGN KEY (`IdVendedor`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `Inventario`
--
ALTER TABLE `Inventario`
  ADD CONSTRAINT `Inventario_ibfk_1` FOREIGN KEY (`IdProducto`) REFERENCES `Productos` (`IdProductos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `moduloXrol`
--
ALTER TABLE `moduloXrol`
  ADD CONSTRAINT `moduloXrol_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `moduloXrol_ibfk_2` FOREIGN KEY (`modulo_id`) REFERENCES `modulos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
