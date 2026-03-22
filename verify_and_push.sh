#!/bin/bash
# Verification and push script

echo "FastAPI Template - Verification & Push"
echo "======================================="
echo ""

# Step 1: Verify .gitignore
echo "[1/5] Verifying .gitignore..."
if grep -q ".idea/" .gitignore; then
    echo "  ✓ .idea/ is ignored"
else
    echo "  ✗ .idea/ not in .gitignore"
fi

if grep -q ".venv/" .gitignore; then
    echo "  ✓ .venv/ is ignored"
else
    echo "  ✗ .venv/ not in .gitignore"
fi

if grep -q "\.env$" .gitignore; then
    echo "  ✓ .env is ignored"
else
    echo "  ✗ .env not in .gitignore"
fi

# Step 2: Check for files that shouldn't be tracked
echo ""
echo "[2/5] Checking for unwanted tracked files..."

unwanted_patterns=(".venv" "__pycache__" "*.pyc" ".env" "*.db" "*.sqlite")
found_unwanted=0

for pattern in "${unwanted_patterns[@]}"; do
    if git ls-files | grep -q "$pattern"; then
        echo "  ⚠ Found tracked files matching: $pattern"
        found_unwanted=1
    fi
done

if [ $found_unwanted -eq 0 ]; then
    echo "  ✓ No unwanted files are tracked"
fi

# Step 3: Show what will be committed
echo ""
echo "[3/5] Files to be pushed:"
git ls-files | head -30
echo "  ... (run 'git ls-files' to see all)"

# Step 4: Confirm push
echo ""
echo "[4/5] Ready to push to GitHub"
echo ""
read -p "Continue with push? [y/N]: " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Push cancelled."
    exit 0
fi

# Step 5: Run setup_repo.sh
echo ""
echo "[5/5] Running setup_repo.sh..."
echo ""

if [ -f "./setup_repo.sh" ]; then
    chmod +x setup_repo.sh
    ./setup_repo.sh
else
    echo "Error: setup_repo.sh not found"
    echo ""
    echo "Run manually:"
    echo "  git checkout -b template"
    echo "  git push -u origin template"
    exit 1
fi
