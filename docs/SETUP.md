# Template Setup Guide

This template includes an automated setup script that configures everything for your new project.

## Quick Setup

After cloning this template, run:

```bash
python setup_template.py
```

The script will:
1. ✓ Collect your project information (name, description, author, etc.)
2. ✓ Rename the package directory
3. ✓ Update all Python imports
4. ✓ Update `pyproject.toml` with your project details
5. ✓ Update Docker files
6. ✓ Update Makefile commands
7. ✓ Update GitHub Actions workflows
8. ✓ Update README.md
9. ✓ Update `.env.example`
10. ✓ Clean up template-specific files

## Interactive Mode (Recommended)

Run the script and follow the prompts:

```bash
python setup_template.py
```

Example interaction:
```
FastAPI Template Setup
======================================

Project name [my-fastapi-project]: awesome-api
Package name [awesome_api]:
Project description [A FastAPI application]: An awesome API for my project
Author name [Your Name]: Jane Doe
Author email [your.email@example.com]: jane@example.com
GitHub username [aoa4eva]: janedoe

Configuration Summary:
======================================
Project Name:    awesome-api
Package Name:    awesome_api
Description:     An awesome API for my project
Author:          Jane Doe <jane@example.com>
GitHub User:     janedoe
======================================

Proceed with setup? [Y/n]: y
```

## Non-Interactive Mode

For automation or CI/CD, use command-line arguments:

```bash
python setup_template.py \
  --name my-api-project \
  --description "My awesome API" \
  --author "Jane Doe" \
  --email jane@example.com \
  --github-user janedoe \
  --non-interactive
```

### Required Arguments (Non-Interactive)

- `--name`: Project name (used for repo, Docker images, etc.)
- `--non-interactive`: Skip all prompts

### Optional Arguments

- `--description`: Project description (default: "A FastAPI application")
- `--author`: Author name (default: "Your Name")
- `--email`: Author email (default: "your.email@example.com")
- `--github-user`: GitHub username (default: "aoa4eva")

## What Gets Updated

### 1. Package Directory
```
src/generaltemplate/  →  src/your-project-name/
```

### 2. Python Imports
```python
# Before
from generaltemplate.config import settings

# After
from your_project_name.config import settings
```

### 3. pyproject.toml
- Project name, description, and version
- Author information
- GitHub repository URLs
- Package references
- Entry points

### 4. Docker Files
- Dockerfile commands
- docker-compose.yml service names
- Container names

### 5. Makefile
- Docker image tags
- Package references in commands

### 6. GitHub Actions
- Workflow names
- Docker image tags
- Repository references

### 7. README.md
- Project title
- Description
- Installation instructions
- Repository URLs

### 8. Environment Config
- `.env.example` with app name and database references

## After Setup

1. **Review Changes**: Check that everything looks correct
   ```bash
   git status
   git diff
   ```

2. **Initialize Git** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit from template"
   ```

3. **Install Dependencies**:
   ```bash
   # Option 1: Using install script
   ./install.sh

   # Option 2: Using pip
   make install-pip

   # Option 3: Using uv
   uv sync --all-extras
   ```

4. **Start Development**:
   ```bash
   # Option 1: Using run script
   ./run.sh

   # Option 2: Direct command
   .venv/bin/uvicorn your_package_name.main:app --reload

   # Option 3: Using make
   make dev
   ```

5. **Visit Your API**:
   - Application: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/api/health

6. **Remove Setup Script** (optional):
   ```bash
   rm setup_template.py SETUP.md
   git commit -am "Remove template setup files"
   ```

## Naming Conventions

### Project Name
- Used for: Repository, Docker images, display
- Format: Kebab-case recommended (e.g., `my-api-project`)
- Characters: Letters, numbers, hyphens

### Package Name
- Used for: Python imports, module names
- Format: Snake_case required (e.g., `my_api_project`)
- Characters: Letters, numbers, underscores only
- Auto-generated from project name if not specified

Examples:
- Project: `awesome-api` → Package: `awesome_api`
- Project: `My Cool API` → Package: `my_cool_api`
- Project: `api-v2` → Package: `api_v2`

## Troubleshooting

### "Package directory already exists"

The target package directory already exists. Either:
1. Choose a different name
2. Remove the existing directory
3. The setup was already run

### "No module named 'generaltemplate'"

After setup, you need to reinstall the package:
```bash
pip install -e .
# or
uv sync
```

### Import errors after setup

Run the setup script again, or manually update imports:
```bash
# Find all Python files with old imports
grep -r "from generaltemplate" src/ tests/

# Replace manually or use sed
find src/ tests/ -name "*.py" -exec sed -i 's/generaltemplate/your_package_name/g' {} +
```

### Docker image name conflicts

After renaming, rebuild Docker images:
```bash
make docker-build
# or
docker-compose build --no-cache
```

## Use as a Cookiecutter Alternative

You can also use this setup script programmatically:

```python
from setup_template import TemplateSetup

setup = TemplateSetup(
    project_name="my-api",
    description="My API project",
    author="Your Name",
    email="your@email.com",
    github_user="aoa4eva",
    interactive=False
)

setup.run()
```

## Resetting the Template

To reset back to template state (not recommended):

```bash
# This will lose all your customizations!
git checkout HEAD -- .
python setup_template.py  # Run setup again
```

## Questions?

- Check the [README.md](README.md) for usage instructions
- Check [PLAN.md](PLAN.md) for architecture decisions
- Open an issue on GitHub
