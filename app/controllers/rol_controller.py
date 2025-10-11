import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_model import Rol
from fastapi.encoders import jsonable_encoder

class RolController:
        
    def create_user(self, rol: Rol):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rol (nombre,descripcion) VALUES (%s, %s)", (rol.nombre, rol.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "Rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol WHERE id = %s", (rol_id,))
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

                raise HTTPException(status_code=404, detail="Rol not found")  
                
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