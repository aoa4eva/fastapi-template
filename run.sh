#!/bin/bash
# Simple run script for the development server

# Check if venv exists and has uvicorn
if [ -f ".venv/bin/uvicorn" ]; then
    echo "Starting FastAPI development server..."
    .venv/bin/uvicorn generaltemplate.main:app --reload --host 0.0.0.0 --port 8000
else
    echo "Error: Please run ./install.sh first to install dependencies"
    exit 1
fi
