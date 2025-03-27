# AI Core RAG Local 🧠🚀

This project is a clean and modular AI core built with hexagonal architecture. It integrates local LLMs (.gguf), context retrieval (RAG), and serves as a backend for intelligent agents and natural language APIs.

## 🚀 Key Features

- Hexagonal architecture
- Supports local LLM models (`llama.cpp`)
- Vector database + context retrieval with ChromaDB
- Redis-based conversation memory
- FastAPI REST interface
- Multi-channel assistant ready (WhatsApp, Telegram, etc.)
- tested with `pytest`

## ⚙️ Stack

- Python 3.10+
- FastAPI + Uvicorn
- llama-cpp-python
- ChromaDB
- Redis
- Poetry
- Pytest

## 🧪 Running locally

```bash
poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


# AI Core RAG Local 🧠🚀

Este proyecto es un núcleo de inteligencia artificial construido con arquitectura hexagonal, diseñado para integrar modelos LLM locales (.gguf), recuperación de contexto (RAG) y servir como backend de agentes inteligentes o asistentes conversacionales.

## 🚀 Características principales

- Arquitectura hexagonal
- Soporte para modelos LLM locales (`llama.cpp`)
- Recuperación de contexto con ChromaDB (RAG)
- Conectado con Redis para gestión de memoria
- API REST construida con FastAPI
- Adaptable a agentes y flujos multicanal (WhatsApp, Telegram, etc.)
- Probado con `pytest`

## ⚙️ Tecnologías

- Python 3.10+
- FastAPI + Uvicorn
- llama-cpp-python
- ChromaDB
- Redis
- Poetry
- Pytest

## 🧪 Cómo probar

```bash
poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
