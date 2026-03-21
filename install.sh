#!/bin/bash
# Simple installation script that avoids Xcode license issues

set -e

echo "Installing FastAPI template dependencies..."

# Create venv if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate venv and install
echo "Installing dependencies..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install fastapi "uvicorn[standard]" pydantic pydantic-settings python-dotenv jinja2 python-multipart
.venv/bin/pip install ruff pytest pytest-cov pytest-asyncio httpx

# Install the package in editable mode
.venv/bin/pip install -e .

echo ""
echo "✓ Installation complete!"
echo ""
echo "To start the development server, run:"
echo "  .venv/bin/uvicorn generaltemplate.main:app --reload"
echo ""
echo "Or activate the virtual environment first:"
echo "  source .venv/bin/activate"
echo "  uvicorn generaltemplate.main:app --reload"
