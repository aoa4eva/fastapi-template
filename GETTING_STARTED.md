# Getting Started with FastAPI Template

Complete guide to create a new project from this template.

## 🚀 Quick Start (5 Minutes)

### Option 1: Using GitHub's "Use this template" Button (Easiest)

1. **Click "Use this template"** on GitHub:
   ```
   https://github.com/aoa4eva/fastapi-template
   ```

2. **Create your repository**:
   - Repository name: `my-awesome-api`
   - Description: Your project description
   - Public or Private
   - Click "Create repository from template"

3. **Clone your new repository**:
   ```bash
   git clone git@github.com:yourusername/my-awesome-api.git
   cd my-awesome-api
   ```

4. **Run the setup script**:
   ```bash
   python setup_template.py
   ```

   Follow the prompts:
   - Project name: `my-awesome-api`
   - Description: Your project description
   - Author: Your Name
   - Email: your@email.com
   - GitHub user: yourusername

5. **Install dependencies**:
   ```bash
   ./install.sh
   ```

   Or manually:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -e ".[dev]"
   ```

6. **Start the development server**:
   ```bash
   ./run.sh
   ```

   Or manually:
   ```bash
   .venv/bin/uvicorn my_awesome_api.main:app --reload
   ```

7. **Visit your API**:
   - Application: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/api/health

**Done!** You now have a fully configured FastAPI project! 🎉

---

## 📋 Detailed Setup

### Option 2: Clone and Setup

If the template isn't on GitHub yet, or you prefer cloning:

```bash
# 1. Clone the template
git clone git@github.com:aoa4eva/fastapi-template.git my-new-project
cd my-new-project

# 2. Remove old git history (optional)
rm -rf .git
git init

# 3. Run setup script
python setup_template.py

# 4. Install dependencies
./install.sh

# 5. Start development
./run.sh
```

### Option 3: Non-Interactive Setup

For automation or CI/CD:

```bash
# Clone
git clone git@github.com:aoa4eva/fastapi-template.git my-project
cd my-project

# Setup non-interactively
python setup_template.py \
  --name my-project \
  --description "My awesome API project" \
  --author "Your Name" \
  --email your@email.com \
  --github-user yourusername \
  --non-interactive

# Install and run
./install.sh && ./run.sh
```

---

## 🛠️ What the Setup Script Does

When you run `python setup_template.py`, it automatically:

1. ✅ **Renames the package**
   - `src/generaltemplate/` → `src/your_project_name/`

2. ✅ **Updates all imports**
   - Changes `from generaltemplate` to `from your_project`
   - Updates all files: Python, configs, docs

3. ✅ **Configures pyproject.toml**
   - Project name and description
   - Author information
   - Repository URLs

4. ✅ **Updates Docker files**
   - Dockerfile commands
   - docker-compose.yml service names
   - Container names

5. ✅ **Updates documentation**
   - README.md with your project details
   - All links and references

6. ✅ **Sets up GitHub integration**
   - GitHub Actions workflows
   - Repository references

7. ✅ **Cleans up template files**
   - Notes which files to remove manually

---

## 📂 Project Structure After Setup

```
my-awesome-api/
├── src/
│   └── my_awesome_api/           # Your renamed package
│       ├── __init__.py
│       ├── main.py               # FastAPI app
│       ├── config.py             # Settings
│       └── api/                  # API routes
│           ├── health.py
│           └── items.py
│
├── tests/                        # Test suite
│   ├── test_main.py
│   └── test_api_items.py
│
├── static/                       # CSS, JS, images
├── templates/                    # HTML templates
├── docs/                         # Documentation
├── examples/                     # Usage examples
│
├── .venv/                        # Virtual environment (after install)
├── pyproject.toml                # Project config (updated)
├── Dockerfile                    # Container build (updated)
├── docker-compose.yml           # Local stack (updated)
├── Makefile                      # Dev commands
│
└── README.md                     # Your project README (updated)
```

---

## 🎯 Next Steps After Setup

### 1. Customize Your API

Replace the example items API with your domain logic:

```python
# src/my_awesome_api/api/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def list_users():
    return {"users": []}
```

Register in `main.py`:
```python
from my_awesome_api.api import users

app.include_router(users.router, prefix="/api", tags=["users"])
```

### 2. Add a Database (Optional)

**PostgreSQL:**

```bash
# 1. Uncomment in pyproject.toml
# [project.optional-dependencies]
# postgres = ["asyncpg>=0.30.0", "sqlalchemy[asyncio]>=2.0.0"]

# 2. Install
pip install -e ".[postgres]"

# 3. Uncomment PostgreSQL in docker-compose.yml

# 4. Update .env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mydb
```

### 3. Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit with your settings
nano .env
```

Example `.env`:
```env
APP_NAME=my-awesome-api
ENVIRONMENT=development
DEBUG=true
SECRET_KEY=your-secret-key-here
```

### 4. Write Tests

```python
# tests/test_users.py
from fastapi.testclient import TestClient
from my_awesome_api.main import app

client = TestClient(app)

def test_list_users():
    response = client.get("/api/users")
    assert response.status_code == 200
```

Run tests:
```bash
make test
# or
.venv/bin/pytest
```

### 5. Run with Docker

```bash
# Build image
make docker-build

# Run container
make docker-run

# Or use docker-compose
make docker-compose-up
```

---

## 💻 Development Workflow

### Daily Development

```bash
# Activate virtual environment
source .venv/bin/activate

# Start dev server with hot-reload
uvicorn my_awesome_api.main:app --reload

# In another terminal, run tests on save
pytest-watch
```

### Before Committing

```bash
# Format code
make format

# Run linter
make lint

# Run tests
make test

# Check coverage
make test-cov
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/add-users

# Make changes, commit
git add .
git commit -m "feat: add user management endpoints"

# Push and create PR
git push origin feature/add-users
gh pr create
```

---

## 🔧 Common Tasks

### Add a New Endpoint

1. Create router file:
   ```python
   # src/my_awesome_api/api/products.py
   from fastapi import APIRouter

   router = APIRouter()

   @router.get("/products")
   async def list_products():
       return {"products": []}
   ```

2. Register in `main.py`:
   ```python
   from my_awesome_api.api import products

   app.include_router(products.router, prefix="/api", tags=["products"])
   ```

### Add Frontend (React/Vue)

```bash
cd frontend
npm create vite@latest . -- --template react-ts
npm install
npm run dev
```

Update `vite.config.js`:
```javascript
export default {
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
}
```

### Add Authentication

Install FastAPI Users:
```bash
pip install fastapi-users[sqlalchemy]
```

See FastAPI Users documentation for setup.

### Deploy to Production

**Docker:**
```bash
docker build -t my-api .
docker run -p 80:8000 my-api
```

**Cloud Platforms:**
- **Heroku**: Add `Procfile` with `web: uvicorn my_awesome_api.main:app`
- **Railway**: Connect GitHub repo, auto-deploys
- **Fly.io**: `fly launch` (detects Dockerfile)
- **Google Cloud Run**: `gcloud run deploy`
- **AWS ECS**: Use Dockerfile

---

## 📚 Learning Resources

### FastAPI
- [Official Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Advanced User Guide](https://fastapi.tiangolo.com/advanced/)
- [Best Practices](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

### Project Structure
- [docs/PLAN.md](docs/PLAN.md) - Architecture decisions
- [docs/SETUP.md](docs/SETUP.md) - Detailed setup guide
- [docs/LIBRARY_USAGE.md](docs/LIBRARY_USAGE.md) - Advanced usage

### Examples
- Check `examples/` directory for more patterns
- See `tests/` for testing examples
- Review `src/generaltemplate/api/items.py` for CRUD patterns

---

## 🆘 Troubleshooting

### "Module not found: my_awesome_api"

You need to install the package:
```bash
pip install -e .
```

### "Port 8000 already in use"

Change the port:
```bash
uvicorn my_awesome_api.main:app --reload --port 8001
```

### "Permission denied: ./install.sh"

Make executable:
```bash
chmod +x install.sh
./install.sh
```

### "setup_template.py didn't rename files"

Run it again or rename manually:
```bash
mv src/generaltemplate src/my_project_name
# Then update imports
```

### Docker build fails

Clear cache and rebuild:
```bash
docker builder prune
make docker-build
```

---

## ✅ Checklist for New Projects

After setup, verify:

- [ ] Setup script completed successfully
- [ ] Package renamed (no `generaltemplate` references)
- [ ] Dependencies installed
- [ ] Dev server starts: `./run.sh`
- [ ] API accessible: http://localhost:8000
- [ ] Tests pass: `make test`
- [ ] Docs generated: http://localhost:8000/docs
- [ ] Environment configured: `.env` created
- [ ] Git initialized: `git init` (if needed)
- [ ] First commit: `git commit -m "Initial commit"`

---

## 🎉 You're Ready!

You now have a production-ready FastAPI project with:
- ✅ Modern Python tooling (uv, ruff)
- ✅ Docker deployment ready
- ✅ CI/CD pipeline configured
- ✅ Comprehensive tests
- ✅ Auto-generated docs
- ✅ Type-safe configuration
- ✅ Development scripts

**Start building your API!** 🚀

---

## 📞 Need Help?

- 📖 **Documentation**: See [docs/](docs/) folder
- 🐛 **Issues**: [GitHub Issues](https://github.com/aoa4eva/fastapi-template/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/aoa4eva/fastapi-template/discussions)
- 📧 **Contact**: Open an issue on GitHub

---

**Happy coding!** 💻
