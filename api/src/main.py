"""
This module sets up the FastAPI application for the Word Counter API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from system_state import system_state_router
from word_counter import word_counter_router

app = FastAPI(
    title="Word Counter API",
    description="A simple API that counts the number of words in a text.",
    version="1.0.0",
    contact={
        "name": "Kevin Ruan Soares",
        "url": "https://github.com/KevinRuanSoares",
        "email": "contato@kevinrsoares.com.br",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(system_state_router, prefix="/api")
app.include_router(word_counter_router, prefix="/api")
