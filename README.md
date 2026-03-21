# FastAPI Project Template

[![CI](https://github.com/aoa4eva/fastapi-template/workflows/CI/badge.svg)](https://github.com/aoa4eva/fastapi-template/actions)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A production-ready FastAPI project template with modern Python tooling, Docker deployment, and flexible frontend options.

## Features

- ⚡ **FastAPI** - Modern, fast web framework for building APIs
- 🚀 **uv** - Lightning-fast Python package management (10-100x faster than pip)
- 🎨 **Ruff** - Extremely fast Python linter and formatter (replaces flake8, black, isort)
- 🐳 **Docker** - Multi-stage builds for optimized production deployment
- 📦 **pydantic-settings** - Type-safe configuration management with .env support
- ✅ **pytest** - Comprehensive test suite with coverage reporting
- 🔄 **GitHub Actions** - CI/CD pipeline for lint, test, and Docker builds
- 🎭 **Frontend Flexibility** - Support for vanilla JS, React, Vue, or any framework
- 📝 **API Documentation** - Auto-generated OpenAPI docs (Swagger UI + ReDoc)

## Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) - Install with: `pip install uv` (optional, pip works too)
- Docker (optional, for containerized deployment)

### Setup Methods

**🚀 Automated Setup (Recommended)**

The template includes an automated setup script that configures everything:

```bash
python setup_template.py
```

See [SETUP.md](SETUP.md) for details.

**📦 Library Usage**

You can also use the template as a Python library:

```python
from generaltemplate.setup import setup_template

setup_template(
    name="my-api",
    author="Your Name",
    email="your@email.com"
)
```

See [LIBRARY_USAGE.md](LIBRARY_USAGE.md) for programmatic usage.

**⚙️ Manual Setup**

### Installation

1. **Clone this template** for your new project:

```bash
git clone https://github.com/aoa4eva/fastapi-template.git my-new-project
cd my-new-project
```

2. **Run the setup script** to configure for your project:

```bash
python setup_template.py
```

This will interactively collect your project information and update all files automatically. See [SETUP.md](SETUP.md) for details.

3. **Install dependencies**:

```bash
make install
```

4. **Configure environment** (optional):

```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run the development server**:

```bash
make dev
```

Visit [http://localhost:8000](http://localhost:8000) to see your API!

## Development

### Available Commands

Run `make help` to see all available commands:

```bash
# Development
make install           # Install dependencies with uv
make dev              # Run development server with hot-reload
make lint             # Run ruff linter
make format           # Format code with ruff
make test             # Run tests with pytest
make clean            # Remove cache and build artifacts

# Docker
make docker-build     # Build Docker image
make docker-run       # Run Docker container
make docker-compose-up   # Start all services with docker-compose
make docker-compose-down # Stop all services
```

### Project Structure

```
generaltemplate/
├── src/
│   └── generaltemplate/          # Main application package
│       ├── __init__.py
│       ├── main.py              # FastAPI app entry point
│       ├── config.py            # Settings management
│       └── api/                 # API routes
│           ├── __init__.py
│           ├── health.py        # Health check endpoints
│           └── items.py         # Example CRUD endpoints
├── static/                       # Static files (CSS, JS, images)
│   ├── style.css
│   └── app.js
├── templates/                    # Jinja2 HTML templates
│   ├── base.html
│   └── index.html
├── tests/                        # Test suite
│   ├── test_main.py
│   └── test_api_items.py
├── frontend/                     # Optional Node.js frontend
│   ├── package.json
│   └── README.md
├── .github/
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
├── Dockerfile                    # Multi-stage Docker build
├── docker-compose.yml           # Local development with Docker
├── Makefile                     # Development commands
├── pyproject.toml               # Project configuration
├── .env.example                 # Environment variables template
└── README.md                    # This file
```

### Adding New API Endpoints

1. Create a new router in `src/generaltemplate/api/`:

```python
# src/generaltemplate/api/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def list_users():
    return {"users": []}
```

2. Register the router in `main.py`:

```python
from generaltemplate.api import users

app.include_router(users.router, prefix=settings.api_prefix, tags=["users"])
```

### Configuration

Configuration is managed through environment variables using `pydantic-settings`. See `.env.example` for all available options.

```python
from generaltemplate.config import settings

# Access settings anywhere in your code
database_url = settings.database_url
debug_mode = settings.debug
```

### Testing

Run tests with coverage:

```bash
make test
```

Run tests with HTML coverage report:

```bash
make test-cov
# Open htmlcov/index.html in your browser
```

Write new tests in the `tests/` directory:

```python
from fastapi.testclient import TestClient
from generaltemplate.main import app

client = TestClient(app)

def test_my_endpoint():
    response = client.get("/api/my-endpoint")
    assert response.status_code == 200
```

## Docker Deployment

### Build and Run

```bash
# Build the Docker image
make docker-build

# Run the container
make docker-run
```

### Docker Compose (with PostgreSQL and Redis)

Edit `docker-compose.yml` to uncomment the services you need:

```yaml
services:
  api:
    # ...
  db:        # Uncomment for PostgreSQL
    # ...
  redis:     # Uncomment for Redis
    # ...
```

Then start all services:

```bash
make docker-compose-up
```

### Production Deployment

The Dockerfile uses a multi-stage build for optimal image size:

- **Builder stage**: Installs dependencies with uv
- **Runtime stage**: Slim Python image (~100MB)
- **Non-root user**: Runs as unprivileged user for security
- **Health check**: Built-in health check endpoint

Deploy to:
- **AWS ECS/Fargate**: Use the Dockerfile directly
- **Google Cloud Run**: Automatically detects the Dockerfile
- **Kubernetes**: Use the image with provided Kubernetes manifests
- **DigitalOcean App Platform**: Push to container registry
- **Fly.io**: `fly launch` automatically detects FastAPI

## Frontend Options

### Option 1: Vanilla JavaScript (Default)

Use the provided `static/` and `templates/` directories:

- Static files in `static/` (CSS, JS)
- HTML templates in `templates/` (Jinja2)
- No build step required
- FastAPI serves everything

**Best for:** Simple applications, prototypes, server-side rendering

### Option 2: Modern JavaScript Framework

Set up React, Vue, or your preferred framework in the `frontend/` directory:

```bash
cd frontend
npm create vite@latest . -- --template react-ts
npm install
npm run dev
```

Configure proxy in `vite.config.js` to connect to the API:

```javascript
export default {
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
}
```

**Best for:** Complex UIs, SPAs, team with frontend specialists

### Option 3: Hybrid Approach

- Use Jinja2 templates for marketing pages
- Use vanilla JS for simple enhancements
- Add a separate SPA for complex features

**Best for:** Content-heavy sites with interactive features

## Database Integration

### PostgreSQL (Recommended for Production)

1. Uncomment PostgreSQL settings in `config.py`
2. Add database dependencies in `pyproject.toml`:

```toml
[project.optional-dependencies]
postgres = [
    "asyncpg>=0.30.0",
    "sqlalchemy[asyncio]>=2.0.0",
]
```

3. Install dependencies:

```bash
uv sync --extra postgres
```

4. Uncomment PostgreSQL service in `docker-compose.yml`

### SQLite (Good for Development)

SQLite works out of the box - no additional setup needed. Just set in `.env`:

```env
DATABASE_URL=sqlite:///./generaltemplate.db
```

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push and PR:

1. **Lint**: Checks code with ruff
2. **Test**: Runs pytest with coverage
3. **Docker**: Builds container image

To enable:

1. Push to GitHub
2. Actions run automatically
3. Add secrets in repository settings if needed

## Customization

### Rename the Project

1. Update `pyproject.toml`:
   - Change `name` field
   - Update `description`, `authors`, URLs

2. Rename package directory:
   ```bash
   mv src/generaltemplate src/your-project-name
   ```

3. Update imports throughout codebase
4. Update `Dockerfile` CMD if needed

### Add Database Models

Install SQLAlchemy and create models:

```python
# src/your-project-name/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
```

### Add Authentication

Consider these libraries:
- **FastAPI Users**: Full-featured auth system
- **FastAPI JWT Auth**: Simple JWT authentication
- **Authlib**: OAuth/OpenID Connect

### Add Background Tasks

Use:
- **Celery**: For distributed task queues
- **FastAPI BackgroundTasks**: For simple async tasks
- **APScheduler**: For scheduled tasks

## Performance Tips

1. **Use async/await**: FastAPI is async-first
2. **Database connection pooling**: Configure in SQLAlchemy
3. **Caching**: Add Redis for frequently accessed data
4. **Response compression**: Enable gzip middleware
5. **Docker image**: Already optimized with multi-stage build

## Security Checklist

- [ ] Change `SECRET_KEY` in production (generate with `openssl rand -hex 32`)
- [ ] Set `DEBUG=false` in production
- [ ] Configure `ALLOWED_HOSTS` for CORS
- [ ] Use HTTPS in production
- [ ] Enable security headers middleware
- [ ] Validate all user inputs (Pydantic handles this)
- [ ] Keep dependencies updated (`uv sync --upgrade`)
- [ ] Run security scans (`pip-audit`)

## Troubleshooting

### uv not found

```bash
pip install uv
```

### Import errors

Make sure you've installed dependencies:

```bash
make install
```

### Port already in use

Change the port in `.env`:

```env
PORT=8001
```

Or specify when running:

```bash
uv run uvicorn generaltemplate.main:app --port 8001
```

### Docker build fails

Clear Docker cache:

```bash
docker builder prune
make docker-build
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`make test`)
5. Format code (`make format`)
6. Commit changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Docker Documentation](https://docs.docker.com)

## Support

- 📖 [Documentation](https://github.com/aoa4eva/generaltemplate/wiki)
- 🐛 [Issue Tracker](https://github.com/aoa4eva/generaltemplate/issues)
- 💬 [Discussions](https://github.com/aoa4eva/generaltemplate/discussions)

---

**Made with ❤️ using FastAPI and modern Python tooling**
