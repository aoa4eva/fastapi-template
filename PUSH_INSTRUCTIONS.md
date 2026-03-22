# Push to GitHub Instructions

## ✅ Pre-Push Checklist

Before pushing, verify:
- [ ] .gitignore is properly configured
- [ ] No .venv/ or __pycache__/ files tracked
- [ ] No .env files with secrets
- [ ] No IDE-specific files (.idea/)
- [ ] All commits have clear messages
- [ ] Documentation is complete

## 🚀 Quick Push

Run the automated script:

```bash
./setup_repo.sh
```

This will:
1. Create `template` branch
2. Stage all template files
3. Commit with detailed message
4. Create GitHub repository: `aoa4eva/fastapi-template`
5. Push to GitHub
6. Set default branch

## 🔍 Verify Before Push

Run the verification script:

```bash
./verify_and_push.sh
```

This checks:
- ✅ .gitignore is correct
- ✅ No unwanted files tracked
- ✅ Shows what will be pushed
- ✅ Confirms before pushing

## 📋 Manual Push (Alternative)

If you prefer manual control:

### Step 1: Verify Files

```bash
# Check what's tracked
git ls-files

# Check what's ignored
git status --ignored

# Verify no secrets
git grep -i "password\|secret\|key" -- ':!*.md' ':!*.example'
```

### Step 2: Create Branch

```bash
git checkout -b template
```

### Step 3: Stage Files

```bash
git add .
```

### Step 4: Commit

```bash
git commit -m "feat: Production-ready FastAPI template

Complete template with automated setup, documentation, and deployment"
```

### Step 5: Create GitHub Repository

Using GitHub CLI:
```bash
gh repo create fastapi-template \
  --public \
  --description "Production-ready FastAPI project template" \
  --source=. \
  --remote=origin \
  --push
```

Or manually:
1. Go to https://github.com/new
2. Name: `fastapi-template`
3. Public repository
4. Don't initialize with README (we have one)
5. Create repository

### Step 6: Add Remote and Push

```bash
# Add remote
git remote add origin git@github.com:aoa4eva/fastapi-template.git

# Push
git push -u origin template

# Set as default branch
gh repo edit --default-branch template
```

## 🔐 Security Check

Before making public, ensure:

```bash
# Check for secrets
git grep -i "password" | grep -v "example\|README"
git grep -i "secret" | grep -v "example\|README"
git grep -i "api.*key" | grep -v "example\|README"

# Check for emails
git grep -i "@.*\.com" | grep -v "example\|noreply"

# Check .env files
git ls-files | grep "\.env$"  # Should return nothing
```

## 📂 What Gets Pushed

✅ **Included:**
- Source code (src/)
- Tests (tests/)
- Documentation (docs/)
- Configuration files
- Scripts (setup_template.py, install.sh, etc.)
- GitHub templates (.github/)
- Examples (examples/)
- Static files (static/)
- Templates (templates/)

❌ **Excluded:**
- .venv/ (virtual environment)
- __pycache__/ (Python cache)
- .env (secrets)
- .idea/ (IDE files)
- *.pyc (compiled Python)
- *.db, *.sqlite (databases)
- node_modules/ (if present)
- .DS_Store (macOS)

## 🎯 After Push

1. **Enable Template Repository**:
   - Go to Settings → General
   - Check "Template repository"
   - This adds "Use this template" button

2. **Add Topics**:
   ```
   fastapi, python, template, docker, api, rest-api,
   python3, uvicorn, pydantic, asyncio
   ```

3. **Configure Branch Protection**:
   - Settings → Branches
   - Add rule for `template`
   - Require PR reviews (optional)

4. **Enable Discussions**:
   - Settings → General → Features
   - Check "Discussions"

5. **Create First Release**:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   gh release create v1.0.0
   ```

## 🆘 Troubleshooting

### "Permission denied (publickey)"

Setup SSH keys:
```bash
ssh-keygen -t ed25519 -C "your@email.com"
gh ssh-key add ~/.ssh/id_ed25519.pub
```

Or use HTTPS:
```bash
git remote set-url origin https://github.com/aoa4eva/fastapi-template.git
```

### "Repository already exists"

```bash
# If you want to replace it
gh repo delete aoa4eva/fastapi-template

# Or just push to existing
git remote add origin git@github.com:aoa4eva/fastapi-template.git
git push -u origin template
```

### "Files too large"

```bash
# Check for large files
git ls-files | xargs ls -lh | sort -k5 -h | tail -10

# Remove large files
git rm --cached path/to/large/file
```

## ✅ Verify Push Success

After pushing, check:

```bash
# Visit repository
gh repo view --web

# Clone in temp location to verify
cd /tmp
git clone git@github.com:aoa4eva/fastapi-template.git test-clone
cd test-clone
python setup_template.py --help
```

## 📞 Support

- Issues: https://github.com/aoa4eva/fastapi-template/issues
- Username: aoa4eva
- Repository: fastapi-template

---

**Ready to share your template!** 🎉
