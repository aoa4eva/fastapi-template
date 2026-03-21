# Project Template Design & Architecture

This document explains the design decisions, architecture choices, and rationale behind the FastAPI project template.

## Table of Contents

- [Overview](#overview)
- [Tool Choices](#tool-choices)
- [Architecture Decisions](#architecture-decisions)
- [Project Structure](#project-structure)
- [Extension Patterns](#extension-patterns)
- [Trade-offs](#trade-offs)

## Overview

This template is designed to be:

1. **Production-Ready**: Works out of the box for real applications
2. **Flexible**: Supports multiple frontend approaches and deployment options
3. **Modern**: Uses latest Python tooling and best practices
4. **Fast**: Optimized for developer experience and runtime performance
5. **Maintainable**: Clear structure, well-documented, easy to extend

## Tool Choices

### 1. Package Management: uv

**Why uv over pip/poetry/pipenv?**

- **Speed**: 10-100x faster than pip, makes `make install` nearly instant
- **Simplicity**: Works like pip but better - no new concepts to learn
- **Lockfiles**: Automatically handles dependency locking (like poetry/pipenv)
- **Modern**: Built by Astral (same team as Ruff), actively maintained
- **Compatible**: Works with standard `pyproject.toml`

**Trade-offs:**
- ✅ Much faster installation and resolution
- ✅ Simpler than poetry (no new commands to learn)
- ⚠️ Relatively new tool (but production-ready)
- ❌ Less mature than pip (but improving rapidly)

**Alternatives considered:**
- **pip**: Too slow, no lockfiles
- **poetry**: Slower, more complex, sometimes conflicts with pip
- **pipenv**: Slower, less actively maintained

### 2. Linting/Formatting: Ruff

**Why Ruff over flake8 + black + isort?**

- **Speed**: 10-100x faster than existing tools
- **Single Tool**: Replaces flake8, black, isort, pyupgrade
- **Drop-in Replacement**: Compatible with existing configs
- **Automatic Fixes**: Can auto-fix many issues
- **Active Development**: Rapidly improving

**Trade-offs:**
- ✅ Much faster linting and formatting
- ✅ One tool instead of three
- ✅ Better error messages
- ⚠️ Newer than alternatives (but widely adopted)
- ⚠️ Occasionally different behavior than black (rare)

**Alternatives considered:**
- **black + flake8 + isort**: Slower, three tools to configure
- **pylint**: Much slower, more opinionated
- **mypy**: Type checking only (can use alongside Ruff)

### 3. Web Framework: FastAPI

**Why FastAPI?**

- **Performance**: One of the fastest Python frameworks
- **Modern Python**: Uses type hints and async/await
- **Auto Documentation**: OpenAPI/Swagger docs generated automatically
- **Validation**: Pydantic models provide automatic validation
- **Developer Experience**: Excellent error messages and auto-completion

**Trade-offs:**
- ✅ Very fast (comparable to Node.js/Go)
- ✅ Great DX with type hints and auto-complete
- ✅ Built-in API documentation
- ⚠️ Async-first can be tricky for beginners
- ❌ More verbose than Flask for simple apps

**Alternatives considered:**
- **Flask**: Simpler but slower, no async, no auto-docs
- **Django**: Full-featured but heavier, not API-focused
- **Starlette**: FastAPI is built on Starlette (lower-level)

### 4. Configuration: pydantic-settings

**Why pydantic-settings over python-decouple/environs?**

- **Type Safety**: Full type checking and validation
- **IDE Support**: Autocomplete for all settings
- **Pydantic Integration**: Works seamlessly with FastAPI
- **Validation**: Automatic validation of environment variables
- **Documentation**: Self-documenting with type hints

**Trade-offs:**
- ✅ Type-safe configuration
- ✅ Validation built-in
- ✅ Great IDE support
- ⚠️ Slightly more boilerplate than simpler solutions
- ⚠️ Requires understanding Pydantic

**Alternatives considered:**
- **python-decouple**: Simpler but no type safety
- **environs**: Good but not Pydantic-native
- **dynaconf**: More features but more complex

## Architecture Decisions

### 1. src Layout

**Structure:**
```
src/
└── generaltemplate/
    ├── __init__.py
    ├── main.py
    ├── config.py
    └── api/
```

**Why src layout?**

- **Import Safety**: Prevents accidental imports from source directory
- **Distribution**: Better for creating packages
- **Testing**: Forces proper package installation
- **Professional**: Industry standard for Python packages

**Trade-offs:**
- ✅ Prevents import errors in production
- ✅ Better for package distribution
- ⚠️ Slightly more setup (need to install package)
- ⚠️ Different from simpler tutorials

### 2. Router Pattern

**Structure:**
```
api/
├── __init__.py
├── health.py
├── items.py
└── users.py  (add as needed)
```

**Why separate routers?**

- **Organization**: Each domain gets its own file
- **Scalability**: Easy to add new endpoints
- **Testing**: Can test routers independently
- **Team Collaboration**: Multiple devs can work on different routers

**Pattern:**
```python
# In api/items.py
router = APIRouter()

@router.get("/items")
async def list_items():
    pass

# In main.py
app.include_router(items.router, prefix="/api", tags=["items"])
```

### 3. Docker Multi-Stage Build

**Why multi-stage?**

- **Image Size**: ~100MB final image vs ~1GB with single stage
- **Security**: Only runtime dependencies in final image
- **Speed**: Faster deployments with smaller images
- **Build Cache**: Dependencies cached separately from code

**Structure:**
1. **Builder Stage**: Install all dependencies with uv
2. **Runtime Stage**: Copy only .venv and code
3. **Non-root User**: Security best practice
4. **Health Check**: Built-in monitoring

**Trade-offs:**
- ✅ Much smaller images
- ✅ More secure
- ✅ Faster deployments
- ⚠️ Slightly more complex Dockerfile
- ⚠️ Debug requires understanding stages

### 4. Frontend Flexibility

**Three supported approaches:**

1. **Vanilla JS** (static/ + templates/)
   - ✅ No build step
   - ✅ Simple deployment
   - ❌ Limited tooling

2. **Modern Framework** (frontend/)
   - ✅ Full ecosystem (React/Vue/etc.)
   - ✅ Better DX
   - ⚠️ Separate dev server
   - ⚠️ More complexity

3. **Hybrid**
   - ✅ Best of both worlds
   - ⚠️ More to manage

**Why this flexibility?**

Different projects have different needs. The template supports all approaches without forcing a choice.

### 5. Docker Compose with Optional Services

**Structure:**
```yaml
services:
  api: # Always enabled
  db: # Commented out by default
  redis: # Commented out by default
```

**Why commented out by default?**

- **Simplicity**: Not every project needs a database
- **Fast Start**: Can run immediately without setup
- **Clear Examples**: Shows how to add services
- **Easy Enable**: Just uncomment when needed

**Trade-offs:**
- ✅ Fast initial setup
- ✅ Doesn't force dependencies
- ⚠️ Requires uncommenting to use
- ⚠️ Need to understand docker-compose

### 6. Configuration with Defaults

**Pattern:**
```python
class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"  # Sensible default
    debug: bool = False  # Secure default
    secret_key: str = "change-me"  # Obvious placeholder
```

**Why provide defaults?**

- **Development**: Works immediately without .env file
- **Production**: Forces explicit configuration (secure defaults)
- **Documentation**: Defaults show expected format
- **Flexibility**: Can override selectively

## Project Structure

### Directory Purpose

```
generaltemplate/
├── src/generaltemplate/     # Application code (installed package)
├── static/                  # Static assets (CSS, JS, images)
├── templates/               # HTML templates (Jinja2)
├── tests/                   # Test suite (pytest)
├── frontend/                # Optional Node.js frontend
├── .github/workflows/       # CI/CD pipelines
├── pyproject.toml          # Project metadata and dependencies
├── Makefile                # Development commands
├── Dockerfile              # Container build
├── docker-compose.yml      # Local development stack
└── .env.example            # Configuration template
```

### Why this structure?

- **Separation**: Code, tests, and static files clearly separated
- **Standards**: Follows Python packaging best practices
- **Scalability**: Easy to add new components
- **Clarity**: Obvious where everything goes

## Extension Patterns

### Adding a Database

1. Uncomment database settings in `config.py`
2. Add SQLAlchemy to dependencies
3. Create `models.py` for database models
4. Create `database.py` for connection handling
5. Add migrations with Alembic

### Adding Authentication

1. Install auth library (FastAPI Users, JWT Auth)
2. Create `auth/` module in src/
3. Add auth router to main.py
4. Add auth dependency to protected routes

### Adding Background Tasks

1. Install Celery or similar
2. Create `tasks/` module
3. Add worker service to docker-compose.yml
4. Queue tasks from API endpoints

### Adding WebSockets

1. Add WebSocket route in main.py
2. Create `websockets/` module
3. Handle connections and messages
4. Test with WebSocket client

## Trade-offs

### What We Optimized For

1. **Developer Experience**
   - Fast installation with uv
   - Quick feedback with ruff
   - Hot-reload in development
   - Clear error messages

2. **Production Readiness**
   - Secure defaults
   - Multi-stage Docker builds
   - Health checks
   - Configuration validation

3. **Flexibility**
   - Multiple frontend options
   - Optional services
   - Extensible structure
   - Clear patterns

### What We Didn't Include

1. **Database ORM** - Too project-specific
   - Add SQLAlchemy, Tortoise, or Prisma as needed
   - Example patterns in README

2. **Authentication** - Many approaches
   - OAuth, JWT, sessions, etc.
   - Template stays unopinionated

3. **Frontend Framework** - Personal/team preference
   - React, Vue, Svelte, or vanilla
   - All equally supported

4. **Specific Business Logic** - Template is generic
   - Items API is just an example
   - Replace with your domain models

## Common Questions

### Why not use Django?

Django is excellent for traditional web apps, but FastAPI is better for:
- API-first applications
- Microservices
- High-performance requirements
- Modern Python features (async, type hints)

### Why not include a specific database?

Different projects need different databases:
- Simple apps: SQLite
- Traditional apps: PostgreSQL
- High-scale: Postgres + Redis
- NoSQL: MongoDB, DynamoDB

The template shows how to add any database without forcing a choice.

### Why Makefile instead of scripts/?

Makefiles are:
- Universally understood
- Self-documenting with `make help`
- Easy to extend
- Standard in many projects

Alternative: Use task runners like `invoke` or `just`

### Why both static/ and frontend/?

Flexibility:
- `static/`: For simple apps, prototypes, server-rendered pages
- `frontend/`: For complex SPAs, modern frameworks
- Both: For hybrid approaches

Choose what fits your project.

## Migration Guide

### From Flask

1. Replace Flask routes with FastAPI routers
2. Change decorators: `@app.route()` → `@router.get()`
3. Use Pydantic models instead of request.json
4. Add type hints to all functions
5. Use async/await for async operations

### From Django

1. Keep models similar (can use Django ORM with FastAPI)
2. Replace views with FastAPI routers
3. Use Pydantic for serialization (instead of DRF serializers)
4. Static files work similarly
5. Templates work similarly (both use Jinja2)

### From Express.js

1. Routes are similar: `app.get()` → `@router.get()`
2. Use Pydantic models instead of manual validation
3. Async/await works the same way
4. Middleware is similar concept
5. Static files work similarly

## Performance Optimization

### Database

- Use connection pooling (SQLAlchemy)
- Add indexes to frequently queried fields
- Use async database drivers (asyncpg for Postgres)
- Cache expensive queries (Redis)

### API

- Enable compression middleware
- Use `response_model` for automatic serialization
- Stream large responses
- Add Redis for caching
- Use CDN for static files

### Docker

- Already optimized with multi-stage build
- Consider using `python:3.13-slim-bookworm`
- Add layer caching in CI/CD
- Use health checks for orchestration

## Security Considerations

### Built-in Protections

- ✅ Pydantic validation prevents injection
- ✅ Non-root Docker user
- ✅ Secure defaults (debug=False)
- ✅ Type safety prevents many bugs

### Add These in Production

- [ ] HTTPS with proper certificates
- [ ] Rate limiting (slowapi, fastapi-limiter)
- [ ] Security headers middleware
- [ ] CORS configuration (uncomment in main.py)
- [ ] Input sanitization for HTML content
- [ ] SQL injection protection (use ORM)
- [ ] Authentication and authorization
- [ ] Secrets management (vault, AWS Secrets Manager)
- [ ] Regular dependency updates
- [ ] Security scanning (Snyk, Dependabot)

## Conclusion

This template balances:
- **Simplicity**: Easy to understand and start with
- **Power**: Can scale to production applications
- **Flexibility**: Supports multiple approaches
- **Modern**: Uses latest best practices

Choose the patterns that fit your project, and extend as needed. The template is a starting point, not a constraint.

---

**Questions or suggestions?** Open an issue or discussion on GitHub!
