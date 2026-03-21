# GitHub Repository Setup Guide

This guide explains how to push the FastAPI template to GitHub.

## Quick Start

Run the automated setup script:

```bash
./setup_repo.sh
```

This will:
1. ✅ Create a clean `template` branch
2. ✅ Stage all template files
3. ✅ Create initial commit
4. ✅ Create GitHub repository
5. ✅ Push to GitHub
6. ✅ Set default branch

## Prerequisites

### Required

- **Git**: Already have this (repo exists)
- **GitHub account**: [Sign up](https://github.com/join) if needed

### Recommended

- **GitHub CLI (gh)**: For repository creation
  ```bash
  # macOS
  brew install gh

  # Linux
  curl -sS https://webi.sh/gh | sh

  # Or download from: https://cli.github.com
  ```

- **Authenticate GitHub CLI**:
  ```bash
  gh auth login
  ```

## Configuration

Before running the script, you can customize:

```bash
# Set your GitHub username (default: voxetti)
export GITHUB_USER="aoa4eva"

# Or edit setup_repo.sh and change:
GITHUB_USER="aoa4eva"
REPO_NAME="fastapi-template"  # Change if desired
```

## Manual Setup (Alternative)

If you prefer manual setup or don't have `gh` CLI:

### 1. Create Branch

```bash
git checkout -b template
```

### 2. Add Files

```bash
# Add all template files
git add .

# Or selectively:
git add src/ tests/ static/ templates/
git add pyproject.toml Makefile Dockerfile docker-compose.yml
git add README.md SETUP.md PLAN.md
git add .gitignore .dockerignore .env.example
git add setup_template.py install.sh run.sh
git add .github/ examples/
```

### 3. Commit

```bash
git commit -m "Initial commit: FastAPI project template"
```

### 4. Create GitHub Repository

Go to [github.com/new](https://github.com/new) and create a repository named `fastapi-template`.

### 5. Add Remote and Push

```bash
# Add remote (replace aoa4eva)
git remote add origin git@github.com:aoa4eva/fastapi-template.git

# Push
git push -u origin template

# Set as default branch (optional)
gh repo edit --default-branch template
```

## After Setup

### 1. Configure Repository

Visit your repository settings:

**Topics** (Settings → General):
```
fastapi, python, template, docker, api, rest-api,
python3, uvicorn, pydantic, asyncio
```

**About** (Edit repository details):
- Description: "Production-ready FastAPI project template with modern Python tooling"
- Website: Add documentation link if you have one
- Check: ✅ Template repository (this allows "Use this template" button)

**Branch Protection** (Settings → Branches):
- Protect the `template` branch
- Require pull request reviews
- Require status checks to pass

**GitHub Pages** (Settings → Pages):
- Source: Deploy from branch
- Branch: template / docs (if you add docs)

### 2. Add Badges to README

Update README.md with actual badge URLs:

```markdown
[![CI](https://github.com/aoa4eva/fastapi-template/workflows/CI/badge.svg)](https://github.com/aoa4eva/fastapi-template/actions)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

### 3. Enable GitHub Features

**Actions** (Actions tab):
- Enable workflows
- CI will run automatically on push

**Discussions** (Settings → General):
- Enable Discussions for community Q&A

**Issues Templates**:
- Already included in `.github/ISSUE_TEMPLATE/`

### 4. Create First Release

```bash
# Tag the release
git tag -a v1.0.0 -m "Release v1.0.0: Initial template release"
git push origin v1.0.0

# Or use GitHub CLI
gh release create v1.0.0 --title "v1.0.0" --notes "Initial release"
```

## Repository Structure

After setup, your repository will have:

```
fastapi-template/
├── .github/
│   ├── workflows/ci.yml           # CI/CD pipeline
│   ├── ISSUE_TEMPLATE/            # Issue templates
│   ├── PULL_REQUEST_TEMPLATE.md   # PR template
│   └── FUNDING.yml                # Sponsorship info
├── src/generaltemplate/           # Source code
├── tests/                         # Test suite
├── static/                        # Static assets
├── templates/                     # HTML templates
├── examples/                      # Usage examples
├── README.md                      # Main documentation
├── SETUP.md                       # Setup guide
├── PLAN.md                        # Design decisions
├── CONTRIBUTING.md                # Contribution guidelines
├── LICENSE                        # MIT License
├── setup_template.py              # Setup script
└── [Other configuration files]
```

## Making it a Template Repository

To allow others to use "Use this template" button:

1. Go to repository **Settings**
2. Under "General" → "Template repository"
3. Check ✅ **Template repository**
4. Save

Now users can click "Use this template" to create projects!

## Sharing the Template

### Via GitHub Template

Users click "Use this template" on GitHub, then:
```bash
cd their-new-repo
python setup_template.py
```

### Via Git Clone

Users clone and setup:
```bash
git clone https://github.com/aoa4eva/fastapi-template.git my-project
cd my-project
python setup_template.py
```

### Via Library

Users install as a library:
```bash
pip install git+https://github.com/aoa4eva/fastapi-template.git
python -m generaltemplate.setup --name my-project
```

## Troubleshooting

### "gh: command not found"

Install GitHub CLI:
```bash
brew install gh  # macOS
```

Or follow manual setup steps above.

### "gh auth: not logged in"

Authenticate with GitHub:
```bash
gh auth login
```

### "Permission denied (publickey)"

Set up SSH keys:
```bash
ssh-keygen -t ed25519 -C "your@email.com"
gh ssh-key add ~/.ssh/id_ed25519.pub
```

Or use HTTPS instead:
```bash
git remote set-url origin https://github.com/aoa4eva/fastapi-template.git
```

### "Repository already exists"

The script will try to add it as a remote instead. Or:
```bash
# Delete existing repo (if you want to start fresh)
gh repo delete aoa4eva/fastapi-template

# Or just push to existing
git push origin template
```

## Maintenance

### Updating the Template

```bash
# Make changes
git add .
git commit -m "feat: add new feature"
git push origin template

# Tag new version
git tag v1.1.0
git push origin v1.1.0
gh release create v1.1.0
```

### Accepting Contributions

See [CONTRIBUTING.md](CONTRIBUTING.md) for contributor guidelines.

## Support

- **Issues**: [github.com/aoa4eva/fastapi-template/issues](https://github.com/aoa4eva/fastapi-template/issues)
- **Discussions**: [github.com/aoa4eva/fastapi-template/discussions](https://github.com/aoa4eva/fastapi-template/discussions)

---

**Ready to share your template with the world!** 🚀
