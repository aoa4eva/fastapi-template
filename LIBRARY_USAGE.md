# Using the Template as a Python Library

The FastAPI template can be used as a Python library to programmatically set up new projects.

## Installation

### Option 1: From Git Repository

```bash
pip install git+https://github.com/yourusername/generaltemplate.git
```

### Option 2: From Local Clone

```bash
git clone https://github.com/yourusername/generaltemplate.git
cd generaltemplate
pip install -e .
```

## Usage Methods

### 1. Command-Line Module

After installation, run the setup as a Python module:

```bash
# Interactive mode
python -m generaltemplate.setup

# Non-interactive mode
python -m generaltemplate.setup \
  --name my-api \
  --description "My awesome API" \
  --author "Jane Doe" \
  --email jane@example.com \
  --github-user janedoe \
  --non-interactive
```

### 2. As a Python Library

Use the library in your Python scripts:

```python
from generaltemplate.setup import setup_template

# Simple usage
setup_template(
    name="my-awesome-api",
    description="An awesome API for my project",
    author="Jane Doe",
    email="jane@example.com",
    github_user="janedoe"
)
```

### 3. Advanced Usage with TemplateSetup Class

For more control, use the `TemplateSetup` class directly:

```python
from pathlib import Path
from generaltemplate.setup import TemplateSetup

# Create setup instance
setup = TemplateSetup(
    root_dir=Path("/path/to/template"),  # Optional, auto-detected if None
    project_name="my-api-project",
    description="My API project",
    author="Jane Doe",
    email="jane@example.com",
    github_user="janedoe",
    interactive=False  # Set to True for interactive prompts
)

# Run the setup
success = setup.run()

if success:
    print("Setup completed successfully!")
else:
    print("Setup failed!")
```

## Automation Examples

### GitHub Template Repository Automation

Create a post-clone script that automatically runs setup:

```python
#!/usr/bin/env python3
"""post-clone.py - Run after cloning the template"""

import os
import sys
from generaltemplate.setup import setup_template

# Get project info from environment or prompt
project_name = os.environ.get("PROJECT_NAME")
if not project_name:
    project_name = input("Enter project name: ")

# Run setup
success = setup_template(
    name=project_name,
    description=input("Enter description: "),
    author=os.environ.get("GIT_AUTHOR_NAME", "Your Name"),
    email=os.environ.get("GIT_AUTHOR_EMAIL", "your@email.com"),
    github_user=os.environ.get("GITHUB_USER", "yourusername"),
)

sys.exit(0 if success else 1)
```

### CI/CD Integration

Use in a GitHub Action or CI pipeline:

```python
# scripts/setup_new_project.py
import sys
from generaltemplate.setup import setup_template

def main():
    # Read from environment variables
    import os

    success = setup_template(
        name=os.environ["PROJECT_NAME"],
        description=os.environ.get("PROJECT_DESC", "A FastAPI project"),
        author=os.environ.get("AUTHOR", "Your Name"),
        email=os.environ.get("EMAIL", "your@email.com"),
        github_user=os.environ.get("GITHUB_USER", "yourusername"),
    )

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
```

`.github/workflows/setup.yml`:
```yaml
name: Setup New Project

on:
  workflow_dispatch:
    inputs:
      project_name:
        description: 'Project name'
        required: true
      description:
        description: 'Project description'
        required: false

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install template
        run: pip install -e .

      - name: Run setup
        env:
          PROJECT_NAME: ${{ github.event.inputs.project_name }}
          PROJECT_DESC: ${{ github.event.inputs.description }}
          AUTHOR: ${{ github.actor }}
          GITHUB_USER: ${{ github.actor }}
        run: python scripts/setup_new_project.py

      - name: Commit changes
        run: |
          git config user.name "${{ github.actor }}"
          git config user.email "${{ github.actor }}@users.noreply.github.com"
          git add .
          git commit -m "Setup project: ${{ github.event.inputs.project_name }}"
          git push
```

### Batch Project Creation

Create multiple projects from the template:

```python
from pathlib import Path
from generaltemplate.setup import TemplateSetup
import shutil

projects = [
    {
        "name": "user-api",
        "description": "User management API",
    },
    {
        "name": "product-api",
        "description": "Product catalog API",
    },
    {
        "name": "order-api",
        "description": "Order processing API",
    },
]

template_dir = Path("/path/to/generaltemplate")
output_dir = Path("/path/to/projects")

for project in projects:
    # Copy template to new directory
    project_dir = output_dir / project["name"]
    shutil.copytree(template_dir, project_dir)

    # Run setup
    setup = TemplateSetup(
        root_dir=project_dir,
        project_name=project["name"],
        description=project["description"],
        author="Your Company",
        email="dev@company.com",
        github_user="yourcompany",
        interactive=False,
    )

    success = setup.run()

    if success:
        print(f"✓ Created {project['name']}")
    else:
        print(f"✗ Failed to create {project['name']}")
```

### Interactive Web Interface

Create a simple web form to generate projects:

```python
from flask import Flask, request, jsonify
from generaltemplate.setup import setup_template
from pathlib import Path
import tempfile
import shutil

app = Flask(__name__)

@app.route('/create-project', methods=['POST'])
def create_project():
    data = request.json

    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy template
        template_src = Path("/path/to/generaltemplate")
        project_dir = Path(tmpdir) / data['name']
        shutil.copytree(template_src, project_dir)

        # Run setup
        success = setup_template(
            name=data['name'],
            description=data.get('description', ''),
            author=data.get('author', 'Your Name'),
            email=data.get('email', 'your@email.com'),
            github_user=data.get('github_user', 'yourusername'),
            root_dir=project_dir,
        )

        if success:
            # Package the project as zip
            shutil.make_archive(f"/tmp/{data['name']}", 'zip', project_dir)
            return jsonify({'success': True, 'download': f"/download/{data['name']}.zip"})
        else:
            return jsonify({'success': False, 'error': 'Setup failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

## API Reference

### setup_template()

```python
def setup_template(
    name: str,
    description: str = "A FastAPI application",
    author: str = "Your Name",
    email: str = "your.email@example.com",
    github_user: str = "yourusername",
    root_dir: Optional[Path] = None,
) -> bool:
    """
    Configure the template for a new project.

    Args:
        name: Project name (e.g., "my-api-project")
        description: Project description
        author: Author name
        email: Author email
        github_user: GitHub username
        root_dir: Root directory of template (auto-detected if None)

    Returns:
        True if setup succeeded, False otherwise
    """
```

### TemplateSetup Class

```python
class TemplateSetup:
    def __init__(
        self,
        root_dir: Optional[Path] = None,
        project_name: Optional[str] = None,
        description: Optional[str] = None,
        author: Optional[str] = None,
        email: Optional[str] = None,
        github_user: Optional[str] = None,
        interactive: bool = True,
    ):
        """
        Initialize template setup.

        Args:
            root_dir: Root directory of template (auto-detected if None)
            project_name: Project name
            description: Project description
            author: Author name
            email: Author email
            github_user: GitHub username
            interactive: Whether to prompt for input (default: True)
        """

    def run(self) -> bool:
        """
        Execute the setup process.

        Returns:
            True if setup succeeded, False otherwise
        """
```

## Best Practices

1. **Always use version control**: Run setup on a fresh git clone or branch
2. **Test your setup**: Run tests after setup to ensure everything works
3. **Backup before setup**: Keep a copy of the template before running setup
4. **Review changes**: Use `git diff` to review all changes made by setup
5. **Validate inputs**: Ensure project names are valid Python identifiers

## Troubleshooting

### Import Error: No module named 'generaltemplate'

The package isn't installed. Install it first:
```bash
pip install -e .
```

### Setup fails with FileNotFoundError

The template files aren't in the expected location. Specify `root_dir`:
```python
setup_template(name="my-api", root_dir=Path("/path/to/template"))
```

### Permission errors during setup

Ensure you have write permissions to the template directory.

## Examples Repository

See the `examples/` directory for more usage examples:
- `examples/basic_setup.py` - Basic setup script
- `examples/batch_create.py` - Create multiple projects
- `examples/github_action.py` - GitHub Action integration
- `examples/web_interface.py` - Flask web interface

## Support

- Documentation: [README.md](README.md)
- Setup Guide: [SETUP.md](SETUP.md)
- Issues: https://github.com/yourusername/generaltemplate/issues
