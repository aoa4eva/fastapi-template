.PHONY: help install dev lint format test clean docker-build docker-run docker-compose-up docker-compose-down

# Default target
help:
	@echo "FastAPI Template - Available Commands"
	@echo "======================================"
	@echo ""
	@echo "Development:"
	@echo "  make install           - Install dependencies with uv"
	@echo "  make dev              - Run development server with hot-reload"
	@echo "  make lint             - Run ruff linter"
	@echo "  make format           - Format code with ruff"
	@echo "  make test             - Run tests with pytest"
	@echo "  make clean            - Remove cache and build artifacts"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build     - Build Docker image"
	@echo "  make docker-run       - Run Docker container"
	@echo "  make docker-compose-up   - Start all services with docker-compose"
	@echo "  make docker-compose-down - Stop all services"
	@echo ""
	@echo "Frontend (if using Node.js):"
	@echo "  make frontend-install - Install npm dependencies"
	@echo "  make frontend-dev     - Run frontend dev server"
	@echo "  make frontend-build   - Build frontend for production"

# Install dependencies (tries uv first, falls back to pip)
install:
	@echo "Installing dependencies..."
	@if command -v uv >/dev/null 2>&1; then \
		echo "Using uv for installation..."; \
		uv sync --all-extras; \
	else \
		echo "uv not found, using pip..."; \
		python3 -m venv .venv 2>/dev/null || true; \
		. .venv/bin/activate && pip install -e ".[dev]"; \
	fi
	@echo "✓ Dependencies installed"

# Install with pip (bypass uv completely)
install-pip:
	@echo "Installing dependencies with pip..."
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ".[dev]"
	@echo "✓ Dependencies installed with pip"

# Run development server
dev:
	@echo "Starting FastAPI development server..."
	@if [ -f .venv/bin/uvicorn ]; then \
		.venv/bin/uvicorn generaltemplate.main:app --reload --host 0.0.0.0 --port 8000; \
	elif command -v uv >/dev/null 2>&1; then \
		uv run uvicorn generaltemplate.main:app --reload --host 0.0.0.0 --port 8000; \
	else \
		echo "Error: Please run 'make install-pip' first"; \
		exit 1; \
	fi

# Run linter
lint:
	@echo "Running ruff linter..."
	@if [ -f .venv/bin/ruff ]; then \
		.venv/bin/ruff check src/ tests/; \
	else \
		uv run ruff check src/ tests/; \
	fi

# Format code
format:
	@echo "Formatting code with ruff..."
	@if [ -f .venv/bin/ruff ]; then \
		.venv/bin/ruff check --fix src/ tests/; \
		.venv/bin/ruff format src/ tests/; \
	else \
		uv run ruff check --fix src/ tests/; \
		uv run ruff format src/ tests/; \
	fi

# Run tests
test:
	@echo "Running tests with pytest..."
	@if [ -f .venv/bin/pytest ]; then \
		.venv/bin/pytest; \
	else \
		uv run pytest; \
	fi

# Run tests with coverage report
test-cov:
	@echo "Running tests with coverage..."
	@if [ -f .venv/bin/pytest ]; then \
		.venv/bin/pytest --cov --cov-report=html; \
	else \
		uv run pytest --cov --cov-report=html; \
	fi
	@echo "✓ Coverage report generated in htmlcov/index.html"

# Clean build artifacts and caches
clean:
	@echo "Cleaning build artifacts and caches..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf build/ dist/ .eggs/
	@echo "✓ Cleanup complete"

# Docker targets
docker-build:
	@echo "Building Docker image..."
	docker build -t generaltemplate:latest .
	@echo "✓ Docker image built: generaltemplate:latest"

docker-run:
	@echo "Running Docker container..."
	docker run -p 8000:8000 --env-file .env generaltemplate:latest

docker-compose-up:
	@echo "Starting services with docker-compose..."
	docker-compose up -d
	@echo "✓ Services started. API available at http://localhost:8000"

docker-compose-down:
	@echo "Stopping docker-compose services..."
	docker-compose down
	@echo "✓ Services stopped"

docker-compose-logs:
	docker-compose logs -f

# Frontend targets (optional - uncomment if using Node.js frontend)
# frontend-install:
# 	@echo "Installing frontend dependencies..."
# 	cd frontend && npm install
#
# frontend-dev:
# 	@echo "Starting frontend development server..."
# 	cd frontend && npm run dev
#
# frontend-build:
# 	@echo "Building frontend for production..."
# 	cd frontend && npm run build

# Combined development (API + Frontend)
# dev-all:
# 	@echo "Starting API and Frontend..."
# 	make -j2 dev frontend-dev
