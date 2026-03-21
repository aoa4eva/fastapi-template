"""
Main FastAPI application entry point.

This module sets up the FastAPI application with:
- API routers
- Static file serving
- Jinja2 template rendering
- CORS middleware
- Health check endpoints
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from generaltemplate.api import health, items
from generaltemplate.config import settings

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="FastAPI project template with modern Python tooling",
    version="0.1.0",
    debug=settings.debug,
)

# CORS middleware (uncomment and configure as needed)
# if settings.allowed_hosts:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=settings.allowed_hosts,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# Mount static files
static_dir = BASE_DIR / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Setup Jinja2 templates
templates_dir = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(templates_dir)) if templates_dir.exists() else None

# Include API routers
app.include_router(health.router, prefix=settings.api_prefix, tags=["health"])
app.include_router(items.router, prefix=settings.api_prefix, tags=["items"])


@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint - returns a simple HTML page.

    If you're using Jinja2 templates, you can render them here:
        return templates.TemplateResponse("index.html", {"request": request})
    """
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>generaltemplate</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="container">
                <h1>🚀 FastAPI Template</h1>
                <p>Your modern Python API template is running!</p>
                <div class="links">
                    <a href="/docs">📚 API Documentation</a>
                    <a href="/redoc">📖 ReDoc</a>
                    <a href="/api/health">💚 Health Check</a>
                </div>
                <div class="info">
                    <p><strong>Environment:</strong> {environment}</p>
                    <p><strong>Debug Mode:</strong> {debug}</p>
                </div>
            </div>
            <script src="/static/app.js"></script>
        </body>
    </html>
    """.format(
        environment=settings.environment,
        debug=settings.debug
    )


def main():
    """
    Entry point for running the application directly.

    For development, use: make dev
    For production, use: uvicorn generaltemplate.main:app
    """
    import uvicorn

    uvicorn.run(
        "generaltemplate.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.is_development,
    )


if __name__ == "__main__":
    main()
