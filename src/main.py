from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.api_v1.api import api_router


app = FastAPI()

# CORS
origins = ["http://localhost:8000"]

app.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)


# ROTAS
app.include_router(api_router, prefix="/api/v1")
