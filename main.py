from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import news

app = FastAPI()

# Configuración de los orígenes permitidos (dominios)
origins = [
    "https://dragon.victum-re.online",
    "http://localhost:5173",
]

# Configuración de los métodos, encabezados y otros parámetros CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)

@app.get('/')
def welcome():
    return {'Welcome to my FASTAPI API!'}

app.include_router(news.router)