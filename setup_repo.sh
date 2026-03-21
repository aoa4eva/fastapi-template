#!/bin/bash
# Setup script to create a clean template branch and push to GitHub

set -e  # Exit on error

echo "FastAPI Template - Repository Setup"
echo "===================================="
echo ""

# Configuration
TEMPLATE_BRANCH="template"
REPO_NAME="fastapi-template"
REPO_DESCRIPTION="Production-ready FastAPI project template with modern Python tooling"
GITHUB_USER="${GITHUB_USER:-aoa4eva}"  # Change this or set GITHUB_USER env var

echo "Configuration:"
echo "  Branch: $TEMPLATE_BRANCH"
echo "  Repo name: $REPO_NAME"
echo "  GitHub user: $GITHUB_USER"
echo ""

# Step 1: Create and switch to template branch
echo "[1/6] Creating clean template branch..."
git checkout -b $TEMPLATE_BRANCH 2>/dev/null || git checkout $TEMPLATE_BRANCH

# Step 2: Add all template files
echo "[2/6] Adding template files to git..."

# Stage all the template files
git add .gitignore
git add .dockerignore
git add .env.example
git add pyproject.toml
git add Makefile
git add Dockerfile
git add docker-compose.yml
git add README.md
git add PLAN.md
git add SETUP.md
git add LIBRARY_USAGE.md
git add QUICKSTART.md
git add LICENSE 2>/dev/null || echo "  Note: LICENSE not found, skipping"

# Add scripts
git add setup_template.py
git add install.sh
git add run.sh

# Add source code
git add src/

# Add static files and templates
git add static/
git add templates/

# Add tests
git add tests/

# Add frontend placeholder
git add frontend/

# Add GitHub workflows
git add .github/

# Add examples
git add examples/

# Add .idea if it exists (user preference from earlier)
git add .idea/ 2>/dev/null || echo "  Note: .idea/ not found or already ignored"

echo "  ✓ Template files staged"

# Step 3: Commit
echo "[3/6] Creating commit..."
git commit -m "Initial commit: FastAPI project template

Features:
- FastAPI with modern Python tooling (uv, ruff)
- Multi-stage Docker builds
- Automated setup script
- Library usage support
- Comprehensive documentation
- CI/CD with GitHub Actions
- Frontend flexibility (vanilla JS, React, Vue)
- Production-ready configuration

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>" 2>/dev/null || echo "  Note: No changes to commit or already committed"

# Step 4: Create GitHub repository
echo "[4/6] Creating GitHub repository..."

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "  Error: GitHub CLI (gh) not found"
    echo "  Install with: brew install gh"
    echo "  Or visit: https://cli.github.com"
    echo ""
    echo "  Alternatively, create the repository manually:"
    echo "    1. Go to https://github.com/new"
    echo "    2. Create repository named: $REPO_NAME"
    echo "    3. Run: git remote add origin git@github.com:$GITHUB_USER/$REPO_NAME.git"
    echo "    4. Run: git push -u origin $TEMPLATE_BRANCH"
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo "  Error: Not authenticated with GitHub CLI"
    echo "  Run: gh auth login"
    exit 1
fi

# Create the repository
gh repo create "$REPO_NAME" \
    --public \
    --description "$REPO_DESCRIPTION" \
    --source=. \
    --remote=origin \
    --push || {
        echo "  Note: Repository might already exist"
        echo "  Checking if remote exists..."

        if ! git remote get-url origin &> /dev/null; then
            echo "  Adding remote..."
            git remote add origin "git@github.com:$GITHUB_USER/$REPO_NAME.git"
        fi
    }

echo "  ✓ Repository ready"

# Step 5: Push to GitHub
echo "[5/6] Pushing to GitHub..."
git push -u origin $TEMPLATE_BRANCH || {
    echo "  Error: Push failed"
    echo "  You may need to:"
    echo "    1. Check your SSH keys: ssh -T git@github.com"
    echo "    2. Or use HTTPS: git remote set-url origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
    exit 1
}

echo "  ✓ Pushed to GitHub"

# Step 6: Set default branch (optional)
echo "[6/6] Setting default branch..."
gh repo edit --default-branch $TEMPLATE_BRANCH 2>/dev/null || echo "  Note: Could not set default branch (may need permissions)"

echo ""
echo "===================================="
echo "✓ Repository Setup Complete!"
echo "===================================="
echo ""
echo "Repository URL: https://github.com/$GITHUB_USER/$REPO_NAME"
echo "Clone URL (SSH): git@github.com:$GITHUB_USER/$REPO_NAME.git"
echo "Clone URL (HTTPS): https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo ""
echo "Next steps:"
echo "  1. Visit: https://github.com/$GITHUB_USER/$REPO_NAME"
echo "  2. Add topics: fastapi, python, template, docker, api"
echo "  3. Enable GitHub Pages (optional): Settings -> Pages -> Deploy from branch"
echo "  4. Add README badges"
echo "  5. Configure branch protection rules (optional)"
echo ""
echo "To use the template:"
echo "  git clone git@github.com:$GITHUB_USER/$REPO_NAME.git my-new-project"
echo "  cd my-new-project"
echo "  python setup_template.py"
echo ""
