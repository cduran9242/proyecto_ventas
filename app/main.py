# app/main.py
from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.rol_routes import router as rol_router
from app.routes.modulos_routes import router as modulo_router
from app.routes.atributos_routes import router as atributos_router
from app.routes.atributosXusuarios_routes import router as atributoXusuario_router
from app.routes.moduloXrol_routes import router as moduloXrol_router
from app.routes.productos_routes import router as productos_router
from app.routes.inventario_routes import router as inventario_router
from app.routes.pedidos_routes import router as pedidos_router
from app.routes.estados_routes import router as estados_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todas las rutas
app.include_router(user_router)
app.include_router(rol_router)
app.include_router(modulo_router)
app.include_router(atributos_router)
app.include_router(atributoXusuario_router)
app.include_router(moduloXrol_router)
app.include_router(productos_router)
app.include_router(inventario_router)
app.include_router(pedidos_router)
app.include_router(estados_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)