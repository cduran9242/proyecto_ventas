import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.modulos_model import Modulos
from fastapi.encoders import jsonable_encoder

class ModuloController:
        
    def create_user(self, modulo: Modulos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO modulos (nombre,descripcion) VALUES (%s, %s)", (modulo.nombre, modulo.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "Modulo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_modulo(self, modulo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol WHERE id = %s", (modulo_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:

                raise HTTPException(status_code=404, detail="Modulo not found")  
                
        except mysql.connector.Error as err:

            conn.rollback()
        finally:
            conn.close()
       
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()