# Quick Start (Without Xcode License)

If you're getting Xcode license prompts, use these simple scripts to bypass `make`:

## Option 1: Use the install.sh script

```bash
./install.sh
./run.sh
```

## Option 2: Manual installation

```bash
# Create virtual environment
python3 -m venv .venv

# Install dependencies
.venv/bin/pip install --upgrade pip
.venv/bin/pip install fastapi "uvicorn[standard]" pydantic pydantic-settings python-dotenv jinja2 python-multipart
.venv/bin/pip install ruff pytest pytest-cov pytest-asyncio httpx
.venv/bin/pip install -e .

# Run the server
.venv/bin/uvicorn generaltemplate.main:app --reload
```

## Option 3: With activation

```bash
# Activate the virtual environment
source .venv/bin/activate

# Install (if not done already)
pip install -e ".[dev]"

# Run
uvicorn generaltemplate.main:app --reload
```

Once running, visit:
- **Application**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## If you have uv installed

```bash
uv sync --all-extras
uv run uvicorn generaltemplate.main:app --reload
```

## What's triggering Xcode?

The Xcode license prompt is likely triggered by:
- Git operations (if git uses Xcode command-line tools)
- The `make` command checking system tools
- Certain shell operations

The scripts above avoid these triggers by using Python directly.
