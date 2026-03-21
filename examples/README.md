# Template Usage Examples

This directory contains examples of using the FastAPI template in different ways.

## Examples

### basic_setup.py
Simple example showing basic usage of the template library.

```bash
python examples/basic_setup.py
```

### batch_create.py
Create multiple projects from the template in one go.

```bash
python examples/batch_create.py
```

Edit the `projects` list in the file to customize which projects to create.

## Creating Your Own Scripts

You can create your own setup scripts using the template library:

```python
from generaltemplate.setup import setup_template

setup_template(
    name="my-project",
    description="My project description",
    author="Your Name",
    email="your@email.com",
    github_user="yourusername"
)
```

See [LIBRARY_USAGE.md](../LIBRARY_USAGE.md) for complete documentation.

## Requirements

Make sure the template is installed:

```bash
# From the template root directory
pip install -e .
```

## More Examples

- **CI/CD Integration**: See `.github/workflows/` for GitHub Actions examples
- **Web Interface**: See `LIBRARY_USAGE.md` for Flask web interface example
- **Environment-based**: Use environment variables for automation

## Tips

1. Always test your setup script on a copy of the template
2. Use version control to track changes
3. Review generated files before committing
4. Customize the template first, then run batch creation
