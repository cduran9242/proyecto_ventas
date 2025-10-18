# app/controllers/pedidos_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class PedidosController:

    # ========== ENCABEZADO PEDIDOS ==========
    
    def create_encabezado_pedido(self, encabezado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el vendedor existe
            cursor.execute("SELECT id FROM usuarios WHERE id = %s", (encabezado.IdVendedor,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El vendedor no existe")

            query = """
            INSERT INTO Encabezado_Pedidos (Tipo_Pedido, IdCliente, IdVendedor, Moneda, TRM, OC_Cliente, Condicion_pago, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                encabezado.Tipo_Pedido,
                encabezado.IdCliente,
                encabezado.IdVendedor,
                encabezado.Moneda,
                encabezado.TRM,
                encabezado.OC_Cliente,
                encabezado.Condicion_pago
            )

            cursor.execute(query, values)
            pedido_id = cursor.lastrowid
            conn.commit()

            return {"mensaje": "Encabezado de pedido creado exitosamente", "IdPedido": pedido_id}

        except mysql.connector.Error as err:
            print(f"Error al crear encabezado de pedido: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear encabezado de pedido")

        finally:
            conn.close()

    def get_encabezado_pedido(self, pedido_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Encabezado_Pedidos WHERE IdPedido = %s", (pedido_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Pedido no encontrado")

            content = {
                "IdPedido": int(result[0]),
                "Tipo_Pedido": result[1],
                "IdCliente": int(result[2]),
                "IdVendedor": int(result[3]),
                "Moneda": result[4],
                "TRM": float(result[5]) if result[5] else None,
                "OC_Cliente": result[6],
                "Condicion_pago": result[7],
                "created_at": str(result[8]),
                "updated_at": str(result[9])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener pedido: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener pedido")

        finally:
            conn.close()

    def get_encabezados_pedidos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Encabezado_Pedidos")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron pedidos")

            payload = [
                {
                    "IdPedido": data[0],
                    "Tipo_Pedido": data[1],
                    "IdCliente": data[2],
                    "IdVendedor": data[3],
                    "Moneda": data[4],
                    "TRM": float(data[5]) if data[5] else None,
                    "OC_Cliente": data[6],
                    "Condicion_pago": data[7],
                    "created_at": str(data[8]),
                    "updated_at": str(data[9])
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar pedidos: {err}")
            raise HTTPException(status_code=500, detail="Error al listar pedidos")

        finally:
            conn.close()

    # ========== DETALLE PEDIDOS ==========

    def create_detalle_pedido(self, detalle):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el pedido existe
            cursor.execute("SELECT IdPedido FROM Encabezado_Pedidos WHERE IdPedido = %s", (detalle.IdPedido,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El pedido no existe")

            # Verificar que el producto existe
            cursor.execute("SELECT IdProductos FROM Productos WHERE IdProductos = %s", (detalle.IdProducto,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El producto no existe")

            query = """
            INSERT INTO Detalle_Pedidos (IdPedido, IdProducto, Numero_Linea, Cantidad_solicitada, Cantidad_confirmada, 
                                       Precio_unitario, Precio_Total, Precio_Extrajero, Precio_Total_extrajero, 
                                       Numero_Documento, Tipo_Documento, Estado_Siguiente, Estado_Anterior, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                detalle.IdPedido,
                detalle.IdProducto,
                detalle.Numero_Linea,
                detalle.Cantidad_solicitada,
                detalle.Cantidad_confirmada,
                detalle.Precio_unitario,
                detalle.Precio_Total,
                detalle.Precio_Extrajero,
                detalle.Precio_Total_extrajero,
                detalle.Numero_Documento,
                detalle.Tipo_Documento,
                detalle.Estado_Siguiente,
                detalle.Estado_Anterior
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Detalle de pedido creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear detalle de pedido: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear detalle de pedido")

        finally:
            conn.close()

    def get_detalles_pedido(self, pedido_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT dp.*, p.Nombre_Producto, p.Codigo_producto 
                FROM Detalle_Pedidos dp 
                INNER JOIN Productos p ON dp.IdProducto = p.IdProductos 
                WHERE dp.IdPedido = %s
            """, (pedido_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron detalles para este pedido")

            payload = [
                {
                    "IdDetalle_Pedidos": data[0],
                    "IdPedido": data[1],
                    "IdProducto": data[2],
                    "Numero_Linea": data[3],
                    "Cantidad_solicitada": float(data[4]),
                    "Cantidad_confirmada": float(data[5]) if data[5] else None,
                    "Precio_unitario": float(data[6]) if data[6] else None,
                    "Precio_Total": float(data[7]) if data[7] else None,
                    "Precio_Extrajero": float(data[8]) if data[8] else None,
                    "Precio_Total_extrajero": float(data[9]) if data[9] else None,
                    "Numero_Documento": data[10],
                    "Tipo_Documento": data[11],
                    "Estado_Siguiente": data[12],
                    "Estado_Anterior": data[13],
                    "created_at": str(data[14]),
                    "updated_at": str(data[15]),
                    "Nombre_Producto": data[16],
                    "Codigo_producto": data[17]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener detalles del pedido: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener detalles del pedido")

        finally:
            conn.close()