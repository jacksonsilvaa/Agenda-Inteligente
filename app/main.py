"""
main.py

Descrição: Arquivo principal da API em Python.
Autor: Jackson Silva dos Santos
Data de criação: 2025-05-15
Versão: 1.0

Este arquivo contém a configuração e inicialização da API, incluindo rotas principais e configurações.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

# CORS (útil se tiver um front separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #Em ambiente produtivo usar domnios especificos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui todas as rotas
#app.include_router(scheduling_router, prefix="/scheduling")
#app.include_router(consult_router, prefix="/consult")
app.include_router(api_router, prefix=settings.API_V1_STR)