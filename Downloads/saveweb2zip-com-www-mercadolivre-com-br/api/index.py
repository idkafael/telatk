"""
Vercel Serverless Function para o backend FastAPI
"""
from mangum import Mangum
import sys
import os

# Adicionar o diretório backend ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from backend.main import app

# Wrapper para Vercel Serverless Functions
handler = Mangum(app, lifespan="off")

